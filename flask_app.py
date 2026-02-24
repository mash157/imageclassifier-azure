from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from werkzeug.utils import secure_filename
import base64
from io import BytesIO

# Load environment variables
load_dotenv('test-classifier/.env')

app = Flask(__name__)
CORS(app)

# Configuration
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

# Get Azure credentials
PREDICTION_ENDPOINT = os.getenv('PredictionEndpoint')
PREDICTION_KEY = os.getenv('PredictionKey')
PROJECT_ID = os.getenv('ProjectID')
MODEL_NAME = os.getenv('ModelName')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    """Handle image classification prediction"""
    try:
        # Check if file is in request
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Allowed: PNG, JPG, JPEG, GIF, BMP'}), 400
        
        # Read file content
        image_data = file.read()
        
        if len(image_data) > MAX_FILE_SIZE:
            return jsonify({'error': 'File too large. Maximum size: 10MB'}), 400
        
        # Create Azure prediction client
        credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_KEY})
        prediction_client = CustomVisionPredictionClient(
            endpoint=PREDICTION_ENDPOINT,
            credentials=credentials
        )
        
        # Get predictions
        results = prediction_client.classify_image(PROJECT_ID, MODEL_NAME, image_data)
        
        # Process predictions
        predictions = [
            {
                'tag': pred.tag_name,
                'confidence': float(pred.probability),
                'percentage': f"{pred.probability * 100:.1f}%"
            }
            for pred in results.predictions
            if pred.probability > 0.001
        ]
        
        # Sort by confidence descending
        predictions.sort(key=lambda x: x['confidence'], reverse=True)
        
        # Get top prediction
        top_prediction = predictions[0] if predictions else None
        
        return jsonify({
            'success': True,
            'predictions': predictions[:5],  # Return top 5
            'topPrediction': top_prediction,
            'totalPredictions': len(predictions)
        })
    
    except Exception as ex:
        return jsonify({
            'error': f'Error processing image: {str(ex)}'
        }), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model': MODEL_NAME,
        'credentials_configured': all([PREDICTION_ENDPOINT, PREDICTION_KEY, PROJECT_ID, MODEL_NAME])
    })

if __name__ == '__main__':
    if not all([PREDICTION_ENDPOINT, PREDICTION_KEY, PROJECT_ID, MODEL_NAME]):
        print("ERROR: Missing Azure credentials in .env file!")
        exit(1)
    
    # Get port from environment variable (for Render.com deployment)
    port = int(os.getenv('PORT', 5000))
    debug_mode = os.getenv('FLASK_ENV', 'development') == 'development'
    
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
