# ✅ Render.com Deployment Checklist

Quick reference for deploying to Render.com

## Pre-Deployment

- [ ] Project pushed to GitHub repository
- [ ] `.gitignore` includes `.env` (don't commit credentials!)
- [ ] `requirements-ui.txt` is updated with all dependencies
- [ ] `render.yaml` is in project root
- [ ] `.env.example` documents all required variables
- [ ] `flask_app.py` uses `PORT` environment variable

## On Render.com Dashboard

1. **Create Web Service**
   - [ ] Connected GitHub repository
   - [ ] Branch selected (main/master)
   - [ ] Auto-detected `render.yaml` ✓

2. **Set Environment Variables**
   ```
   [ ] PredictionEndpoint = https://your-resource-prediction.cognitiveservices.azure.com/
   [ ] PredictionKey = your-prediction-key-here
   [ ] ProjectID = your-project-id-here
   [ ] ModelName = your-model-name-here
   ```

3. **Verify Settings**
   - [ ] Build Command: `pip install -r requirements-ui.txt`
   - [ ] Start Command: `gunicorn flask_app:app`
   - [ ] Python Version: 3.11 (optional, auto-detected)
   - [ ] Region: Choose nearest to you

4. **Deploy**
   - [ ] Click "Create Web Service"
   - [ ] Monitor build in Logs tab
   - [ ] Wait for green "Active" status

## Post-Deployment

- [ ] Visit your URL: `https://your-app.onrender.com`
- [ ] Test image upload functionality
- [ ] Check predictions work correctly
- [ ] Monitor Logs for any errors

## Troubleshooting

**If build fails:**
- [ ] Check Logs for error message
- [ ] Verify all dependencies in `requirements-ui.txt`
- [ ] Ensure `flask_app.py` has correct imports

**If predictions fail:**
- [ ] Check environment variables are set correctly
- [ ] Verify Azure credentials are still valid
- [ ] Check Logs for Azure authentication errors

**If app is slow:**
- [ ] Free tier has limited resources
- [ ] Consider upgrading to Starter tier
- [ ] Check if predictions take long due to model size

## Enable Auto-Deploy

```bash
# Push changes to GitHub
git push origin main

# Render automatically detects and redeploys
```

## Production Optimizations (Optional)

- [ ] Add custom domain (Settings → Custom Domain)
- [ ] Enable HTTPS (auto-enabled by Render)
- [ ] Monitor metrics (Dashboard → Metrics)
- [ ] Set up alerts for high CPU/memory
- [ ] Consider add-on services (Redis for caching)

## Helpful Links

- Build logs: Dashboard → Logs
- Environment variables: Dashboard → Environment
- Metrics: Dashboard → Metrics
- Support: https://docs.render.com

---

**Status**: Ready for deployment ✅

**Next step**: Push to GitHub and create Web Service on Render.com
