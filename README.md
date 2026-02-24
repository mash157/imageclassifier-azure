# 🤖 AI Image Classifier - Modern Web UI

A beautiful, responsive web interface for Azure Custom Vision image classification with multiple deployment options.

## Features ✨

- **Modern Glassmorphism Design** - Sleek, contemporary UI with frosted glass effect
- **Gradient Background** - Eye-catching purple-to-blue gradient aesthetic
- **Responsive Layout** - Perfectly optimized for desktop, tablet, and mobile
- **Smooth Animations** - Fluid transitions and hover effects
- **Real-time Predictions** - See confidence percentages and classification results
- **Professional Styling** - Built with Poppins font and modern CSS
- **Multiple Deployment Options** - Choose between Streamlit, Flask, or standalone HTML

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements-ui.txt
```

### 2. Configure Environment Variables

Make sure your `.env` file exists in the `test-classifier/` directory with:

```
PredictionEndpoint='https://customvision90-prediction.cognitiveservices.azure.com/'
PredictionKey='your-prediction-key-here'
ProjectID='913c1b14-036e-4876-8c21-9f40b14b2d7b'
ModelName='fruit-classifier'
```

## Usage Options

### Option 1: Streamlit App (Recommended) 🎨

Best for: Rapid development, easy deployment, beautiful UI with minimal code

```bash
streamlit run app.py
```

The app will:
- Open in your browser at `http://localhost:8501`
- Show a modern gradient background
- Display a large, bold title
- Provide image upload functionality
- Show predictions with animated confidence bars
- Display footer with "Built with ❤️ Mash157"

**Features:**
- Custom CSS with glassmorphism effects
- Animated confidence bars
- Top 5 predictions displayed
- Responsive design for all devices
- Beautiful error handling

### Option 2: Standalone HTML UI 🌐

Best for: Static deployment, CDN hosting, embedded use

Simply open `index.html` in your browser:

```bash
# Windows
start index.html

# macOS
open index.html

# Linux
xdg-open index.html
```

Or open it directly in your browser by typing the file path in the address bar.

**Features:**
- No server required for UI (pure frontend)
- Works offline for UI/UX
- Drag-and-drop image support
- Mock predictions (update JavaScript to call actual API)
- Smooth animations
- Mobile responsive

### Option 3: Flask Web App 🚀

Best for: Full-stack deployment, REST API, production use

```bash
python flask_app.py
```

The app will:
- Start a Flask server at `http://localhost:5000`
- Serve the HTML UI with backend prediction support
- Provide REST API endpoints for image classification
- Handle CORS for cross-origin requests

**API Endpoints:**

```
GET /                    - Serve the HTML interface
POST /api/predict        - Classify an image
GET /api/health          - Health check
```

**Example API Usage:**

```bash
# Upload and predict
curl -X POST -F "file=@image.jpg" http://localhost:5000/api/predict

# Health check
curl http://localhost:5000/api/health
```

## Design Features 🎨

### Glassmorphism Effect
- Semi-transparent background with blur effect
- Elegant frosted glass appearance
- Modern and sophisticated look

### Gradient Background
- Purple to blue gradient (135deg)
- Dynamic animation on page load
- Mobile-optimized rendering

### Responsive Breakpoints
- **Desktop**: Full-width optimized layout
- **Tablet** (768px): Adjusted font sizes and spacing
- **Mobile** (480px): Compact design for small screens

### Interactive Elements
- Hover animations on buttons and cards
- Drag-and-drop file upload
- Animated confidence bars
- Smooth transitions (0.3-0.8s easing)

## File Structure

```
image-classification/python/
├── app.py                  # Streamlit application
├── flask_app.py           # Flask web server
├── index.html             # Standalone HTML UI
├── requirements-ui.txt    # Python dependencies
├── README.md              # This file
└── test-classifier/
    ├── .env               # Environment variables
    ├── test-classifier.py # Original classifier
    └── test-images/       # Sample images
```

## Customization

### Change Color Scheme

**In Streamlit (app.py):**
```css
/* Change gradient colors */
background: linear-gradient(135deg, #YOUR_COLOR1 0%, #YOUR_COLOR2 100%);
```

**In HTML (index.html):**
Search for `#667eea` (purple) and `#764ba2` (dark purple) and replace with your colors.

### Modify Footer

**Streamlit:**
```python
st.markdown("""
    <div class="footer">
        <p>Your custom footer text here</p>
    </div>
    """, unsafe_allow_html=True)
```

**HTML:**
```html
<div class="footer">
    <p>Your custom footer text</p>
</div>
```

### Add More Predictions

**Streamlit:**
```python
for tag_name, confidence in predictions_list[:10]:  # Show top 10 instead of 5
```

**HTML:**
Update the JavaScript `displayResults` function to handle more predictions.

## Troubleshooting

### "PermissionDenied" Error
- Verify you're using the **Prediction Key**, not Training Key
- Check that the Prediction Endpoint matches your Azure resource
- Ensure the key hasn't been regenerated

### Module Not Found
```bash
pip install -r requirements-ui.txt
```

### Port Already in Use (Flask)
```bash
python flask_app.py  # Uses port 5000 by default
```

Change port in `flask_app.py`:
```python
app.run(port=5001)
```

### Slow Predictions
- Check your internet connection to Azure
- Verify your model is published in Custom Vision
- Consider caching results for frequently classified images

## Best Practices

1. **Security**: Never commit `.env` files with real keys
2. **Performance**: Compress images before uploading (< 5MB optimal)
3. **UX**: Add loading indicators for users
4. **Testing**: Test on actual devices, not just browser dev tools
5. **Deployment**: Use environment variables for all sensitive data

## Deployment Options

### Streamlit Cloud
```bash
streamlit run app.py --logger.level=error
```
[Deploy to Streamlit Cloud](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app)

### Azure App Service
Deploy `flask_app.py` with a requirements.txt file.

### GitHub Pages (HTML only)
Push `index.html` to your repository and enable GitHub Pages.

### Docker
```dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements-ui.txt .
RUN pip install -r requirements-ui.txt
COPY . .
CMD ["streamlit", "run", "app.py"]
```

## Credits

Built with ❤️ by Mash157

Powered by:
- [Azure Custom Vision](https://www.customvision.ai)
- [Streamlit](https://streamlit.io)
- [Flask](https://flask.palletsprojects.com)
- [Google Fonts - Poppins](https://fonts.google.com/specimen/Poppins)

## License

This project is open source and available under the MIT License.

---

**Happy Classifying!** 🎉
