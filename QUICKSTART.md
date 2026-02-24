# Quick Start Guide 🚀

## 30-Second Setup

### Prerequisites
- Python 3.8+
- Azure Custom Vision credentials in `.env`

### Run Streamlit App (Easiest)

```bash
# 1. Install dependencies (first time only)
pip install -r requirements-ui.txt

# 2. Run the app
streamlit run app.py

# 3. Open browser to: http://localhost:8501
```

### Run Flask App

```bash
# 1. Install dependencies (first time only)
pip install -r requirements-ui.txt

# 2. Run the server
python flask_app.py

# 3. Open browser to: http://localhost:5000
```

### Use HTML UI Only

```bash
# No installation needed!
# Simply open in browser:
# - Windows: Double-click index.html
# - Mac/Linux: Open with your browser

# Note: Predictions won't work without backend.
# Connect to Flask API by updating the JavaScript.
```

---

## Which Option Should I Choose?

| Feature | Streamlit | Flask | HTML |
|---------|-----------|-------|------|
| Setup Time | ⚡ Fastest | 🔧 Medium | 💨 Instant |
| Backend API | ✅ Built-in | ✅ Yes | ❌ Manual |
| Deployment | ☁️ Easy (Cloud) | 🐳 Docker/VPS | 📄 Static |
| Customization | 🎨 Python | 🎨 HTML/CSS | 🎨 HTML/CSS |
| Production Ready | ✅ Yes | ✅✅ Yes | ⚠️ Needs backend |

**Recommendation**: Start with **Streamlit** for quickest setup, use **Flask** for production.

---

## Troubleshooting

### "No such file or directory" error
```bash
# Make sure you're in the right directory:
cd image-classification/python
streamlit run app.py
```

### "Module not found" error
```bash
# Reinstall requirements:
pip install -r requirements-ui.txt --upgrade
```

### "PermissionDenied" from Azure
- Check your `.env` file has correct prediction key & endpoint
- Verify key is **Prediction**, not **Training**
- Check Azure Portal that resource is active

### Port already in use
```bash
# For Streamlit:
streamlit run app.py --server.port 8502

# For Flask:
# Edit flask_app.py, change: app.run(port=5001)
```

---

## Next Steps

✅ **Done!** Your classifier is running.

👉 Try these:
1. Upload a test image
2. See predictions appear
3. Customize colors in CSS
4. Deploy to cloud (Streamlit Cloud, Azure App Service, etc.)

---

Need help? Check the full [README.md](README.md) 📖
