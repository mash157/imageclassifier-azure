# 🚀 Deploying to Render.com

Complete guide to deploy your AI Image Classifier on Render.com

## Prerequisites

✅ Git repository on GitHub with your project  
✅ Azure Custom Vision credentials (Prediction Key, Endpoint, Project ID, Model Name)  
✅ Render.com account (free tier available)

## Step-by-Step Deployment

### 1. Prepare Your GitHub Repository

```bash
# Make sure these files are in your repo:
# - flask_app.py
# - requirements-ui.txt
# - render.yaml
# - templates/index.html
# - .env.example (for reference)
# - .gitignore (exclude .env files)

# Add to .gitignore if not already there:
echo ".env" >> .gitignore
echo "*.pyc" >> .gitignore
echo "__pycache__/" >> .gitignore

git add .
git commit -m "Add Render deployment configuration"
git push
```

### 2. Create Render Account

1. Go to [Render.com](https://render.com)
2. Sign up or log in with GitHub
3. Click **"New +"** → **"Web Service"**

### 3. Connect Your Repository

1. Select your GitHub repository from the list
2. Choose your branch (usually `main` or `master`)
3. Render will auto-detect the `render.yaml` file

### 4. Configure Environment Variables

In the Render dashboard, add these under **Environment**:

```
PredictionEndpoint = https://your-resource-name-prediction.cognitiveservices.azure.com/
PredictionKey = your-actual-prediction-key
ProjectID = your-project-id
ModelName = your-model-name
PYTHON_VERSION = 3.11
FLASK_ENV = production
```

⚠️ **Important**: Use your actual Azure credentials, not placeholder values

### 5. Deploy

1. Click **"Create Web Service"**
2. Render will automatically:
   - Build your project (`pip install -r requirements-ui.txt`)
   - Start the Flask server with gunicorn
   - Assign a URL (e.g., `https://ai-image-classifier.onrender.com`)

### 6. Monitor Deployment

- Check the **Logs** tab to watch the build process
- Once deployed, you'll see a green checkmark
- Your app will be live at the assigned URL

---

## Troubleshooting

### Issue: "ModuleNotFoundError" during deployment

**Solution**: Ensure `requirements-ui.txt` includes all dependencies:
```bash
pip freeze > requirements-ui.txt
```

### Issue: Azure authentication fails

**Solution**: Double-check environment variables in Render dashboard
- Use **Prediction Key** (not Training Key)
- Verify endpoint URL includes `/` at the end
- Check that Project ID and Model Name match your Azure resource

### Issue: Service keeps restarting

**Solution**: Check logs for errors. Common issues:
- Missing environment variables
- Invalid credentials
- Model not published in Custom Vision

### Issue: Timeout on predictions

**Solution**: 
- Render free tier has limited CPU resources
- Upgrade to a paid plan for faster performance
- Or keep default tier and accept slightly slower responses

---

## Deployment Options

### Option 1: Web Service (Recommended)
- Best for Flask/production apps
- Auto-scaling available
- Uses `render.yaml` configuration

### Option 2: Environment Variables Only

If you prefer not to use `render.yaml`:

1. Go to **Settings** → **Environment**
2. Add variables manually:
   - `PORT` (auto-set, don't add)
   - `PredictionEndpoint`
   - `PredictionKey`
   - `ProjectID`
   - `ModelName`
3. Build Command: `pip install -r requirements-ui.txt`
4. Start Command: `gunicorn flask_app:app`

---

## Production Optimization

### Enable HTTPS
Render automatically provides HTTPS. Your app is secure by default.

### Add Custom Domain
1. In Render dashboard → **Settings** → **Custom Domain**
2. Point your domain to Render
3. Enable auto SSL

### Monitor Performance
- Check **Metrics** tab for CPU, memory, request count
- Use **Logs** to debug issues
- Set up alerts for high resource usage

### Scale Your App
- Free tier: Limited CPU/memory
- Upgrade to **Starter** tier for better performance
- Add **Redis** cache for faster predictions

---

## Auto-Deploy from Git

Your app will automatically redeploy when you push to your repository:

```bash
# Make changes locally
git add .
git commit -m "Update styles"
git push origin main

# Render automatically detects changes and redeploys
```

---

## Environment Variables Reference

| Variable | Example | Notes |
|----------|---------|-------|
| `PredictionEndpoint` | `https://customvision90-prediction.cognitiveservices.azure.com/` | Must end with `/` |
| `PredictionKey` | `2pwRaF...` | Use **Prediction** key, not Training |
| `ProjectID` | `913c1b14-...` | Found in Custom Vision portal |
| `ModelName` | `fruit-classifier` | Published model name |
| `PORT` | `5000` | Auto-set by Render, don't change |
| `FLASK_ENV` | `production` | Set to `production` for deployment |
| `PYTHON_VERSION` | `3.11` | Specify Python version |

---

## Monitoring Your Deployment

### Check Logs
```
Dashboard → Logs tab → Filter by date/severity
```

### View Metrics
```
Dashboard → Metrics tab → CPU, Memory, Requests
```

### Test Your App
```bash
# After deployment, test the API:
curl -X POST -F "file=@image.jpg" https://your-app.onrender.com/api/predict
curl https://your-app.onrender.com/api/health
```

---

## Cost Considerations

### Free Tier
- CPU: Shared (low priority)
- Memory: 512 MB
- Price: **$0/month**
- Limitations: Sleeps after 15 minutes inactivity

### Starter Tier
- CPU: 0.5 vCPU dedicated
- Memory: 512 MB
- Price: **$7/month**
- Always running, better performance

### Upgrade Decision
Consider upgrading if:
- You want instant responses (no startup delay)
- You expect frequent use
- You need better performance for image processing

---

## Next Steps

✅ **Done!** Your app is live on Render.com  
👉 Share the URL: `https://your-app.onrender.com`  
🔄 Enable auto-deploy by pushing to GitHub  
📈 Monitor usage in the Render dashboard  
💰 Decide whether to upgrade from free tier

---

## Quick Reference: File Checklist

Make sure these files are in your repository:

```
project-root/
├── flask_app.py              ✅ Main Flask app
├── requirements-ui.txt       ✅ Dependencies
├── render.yaml              ✅ Render configuration
├── templates/
│   └── index.html           ✅ Web UI
├── index.html               ✅ Standalone HTML (optional)
├── .env.example             ✅ Reference (don't commit .env)
├── .gitignore               ✅ Exclude sensitive files
├── README.md                ✅ Documentation
└── [other project files]
```

---

## Support

**Render.com Support**: https://docs.render.com  
**Azure Documentation**: https://docs.microsoft.com/azure  
**Flask Deployment**: https://flask.palletsprojects.com/deployment

---

**Happy deploying!** 🎉
