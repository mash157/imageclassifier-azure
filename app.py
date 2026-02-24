import streamlit as st
import os
from PIL import Image
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from dotenv import load_dotenv

# Load environment variables
load_dotenv('test-classifier/.env')

# Page configuration
st.set_page_config(
    page_title="AI Image Classifier",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS with gradient background and glassmorphism
st.markdown("""
    <style>
        /* Main background with gradient */
        .stApp {
            background: linear-gradient(135deg, #06B6D4 0%, #7C3AED 100%);
            min-height: 100vh;
        }
        
        /* Main container styling */
        .main {
            background: linear-gradient(135deg, #06B6D4 0%, #7C3AED 100%);
            text-align: center;
            margin-bottom: 2rem;
            animation: fadeInDown 0.8s ease-in-out;
        }
        
        h1 {
            font-size: 3.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #ffffff 0%, #e0e7ff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
            letter-spacing: -2px;
        }
        
        .subtitle {
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.1rem;
            font-weight: 300;
            letter-spacing: 1px;
        }
        
        /* Glassmorphism card */
        .glass-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 2rem;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            animation: slideUp 0.8s ease-in-out;
        }
        
        /* Upload section */
        .upload-section {
            text-align: center;
            padding: 2rem;
        }
        
        .upload-section h2 {
            color: rgba(255, 255, 255, 0.95);
            font-size: 1.5rem;
            margin-bottom: 1rem;
            font-weight: 700;
        }
        
        /* Button styling */
        .stButton > button {
            background: linear-gradient(135deg, #06B6D4 0%, #7C3AED 100%);
            color: white !important;
            border: none;
            border-radius: 12px;
            padding: 0.75rem 2rem;
            font-weight: 600;
            font-size: 1rem;
            width: 100%;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(6, 182, 212, 0.4);
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(6, 182, 212, 0.6);
        }
        
        .stButton > button:active {
            transform: translateY(0);
        }
        
        /* Result card */
        .result-card {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 2rem;
            margin-top: 2rem;
            animation: slideUp 0.6s ease-in-out;
        }
        
        .result-card h3 {
            color: rgba(255, 255, 255, 0.95);
            font-size: 1.3rem;
            margin-bottom: 1rem;
            font-weight: 700;
        }
        
        /* Prediction item */
        .prediction-item {
            background: rgba(255, 255, 255, 0.08);
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            border-left: 4px solid #667eea;
            transition: all 0.3s ease;
        }
        
        .prediction-item:hover {
            background: rgba(255, 255, 255, 0.12);
            transform: translateX(5px);
        }
        
        .prediction-label {
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
        
        .confidence-bar {
            background: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            height: 8px;
            overflow: hidden;
            margin-bottom: 0.5rem;
        }
        
        .confidence-fill {
            background: linear-gradient(90deg, #06B6D4 0%, #7C3AED 100%);
            height: 100%;
            border-radius: 10px;
            transition: width 0.5s ease;
        }
        
        .confidence-text {
            color: rgba(255, 255, 255, 0.8);
            font-size: 0.95rem;
            font-weight: 500;
        }
        
        /* Image preview */
        .image-preview {
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
            margin: 1.5rem 0;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid rgba(255, 255, 255, 0.2);
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.95rem;
            animation: fadeIn 1s ease-in-out 0.5s both;
        }
        
        /* Animations */
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
        
        /* Responsive design */
        @media (max-width: 768px) {
            h1 {
                font-size: 2.5rem;
            }
            
            .glass-card {
                padding: 1.5rem;
            }
            
            .stButton > button {
                padding: 0.6rem 1.5rem;
                font-size: 0.95rem;
            }
        }
        
        /* Hide Streamlit elements */
        #MainMenu {
            visibility: hidden;
        }
        
        footer {
            visibility: hidden;
        }
    </style>
    """, unsafe_allow_html=True)

# Main page content
st.markdown("""
    <div class="title-container">
        <h1>🤖 Image Classifier</h1>
        <p class="subtitle">Powered by Azure Custom Vision AI</p>
    </div>
    """, unsafe_allow_html=True)

# Get Configuration Settings
prediction_endpoint = os.getenv('PredictionEndpoint')
prediction_key = os.getenv('PredictionKey')
project_id = os.getenv('ProjectID')
model_name = os.getenv('ModelName')

# Check if credentials are available
if not all([prediction_endpoint, prediction_key, project_id, model_name]):
    st.error("❌ Missing configuration. Please check your .env file.")
    st.stop()

# Glass card container for upload
st.markdown("""
    <div class="glass-card">
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="upload-section">
        <h2>📤 Upload an Image</h2>
    </div>
    """, unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png", "gif", "bmp"])

if uploaded_file is not None:
    try:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.markdown('<div class="image-preview">', unsafe_allow_html=True)
        st.image(image, use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Make prediction
        image_data = uploaded_file.read()
        
        # Authenticate client
        credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
        prediction_client = CustomVisionPredictionClient(
            endpoint=prediction_endpoint,
            credentials=credentials
        )
        
        # Get predictions
        results = prediction_client.classify_image(project_id, model_name, image_data)
        
        # Filter predictions with > 0.1% confidence
        predictions_list = [
            (pred.tag_name, pred.probability * 100)
            for pred in results.predictions
            if pred.probability > 0.001
        ]
        
        # Sort by confidence descending
        predictions_list.sort(key=lambda x: x[1], reverse=True)
        
        # Display results
        st.markdown("""
            <div class="result-card">
                <h3>✅ Prediction Results</h3>
            </div>
            """, unsafe_allow_html=True)
        
        for tag_name, confidence in predictions_list[:5]:  # Show top 5
            st.markdown(f"""
                <div class="prediction-item">
                    <div class="prediction-label">{tag_name}</div>
                    <div class="confidence-bar">
                        <div class="confidence-fill" style="width: {confidence}%"></div>
                    </div>
                    <div class="confidence-text">Confidence: {confidence:.1f}%</div>
                </div>
                """, unsafe_allow_html=True)
        
        # Top prediction
        if predictions_list:
            top_pred, top_conf = predictions_list[0]
            st.success(f"🎯 Primary Classification: **{top_pred}** ({top_conf:.1f}%)")
    
    except Exception as ex:
        st.error(f"❌ Error processing image: {str(ex)}")

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>Built with ❤️ by Mash157 | Powered by Azure Custom Vision</p>
    </div>
    """, unsafe_allow_html=True)
