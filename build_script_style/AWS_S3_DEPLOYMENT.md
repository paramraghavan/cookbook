# 🚀 AWS S3 Deployment Guide - Fixed for PWA

## ⚠️ The Problem You're Experiencing

When hosting on AWS S3, the "Add to Home Screen" shortcut shows **"aws.amazon.com"** instead of your cookbook name.

**Root Cause:**
- S3 static website URLs are long (e.g., `bucket-name.s3-website-region.amazonaws.com`)
- The PWA manifest was using absolute paths (`/`) instead of relative paths (`./`)
- Browser interprets the domain as the app name

## ✅ The Fix (Already Applied!)

I've updated the generator to use **relative paths** in `manifest.json`:

```json
{
  "start_url": "./",    // Was: "/"
  "scope": "./",        // Added this
  ...
}
```

This makes the PWA work correctly on **any domain**, including S3!

---

## 🎯 AWS S3 Deployment - Step by Step

### Option 1: S3 + CloudFront (RECOMMENDED)

This is the **best solution** for PWAs on AWS!

#### Step 1: Create S3 Bucket
```bash
# In AWS Console:
1. Go to S3
2. Create bucket (e.g., "my-vegetarian-cookbook")
3. Enable "Static website hosting"
4. Set index.html as index document
```

#### Step 2: Upload Your Files
```bash
# Upload everything from deploy/ folder
aws s3 sync ./deploy s3://my-vegetarian-cookbook --acl public-read
```

#### Step 3: Set Correct MIME Types (CRITICAL!)
S3 needs to serve files with correct content types:

**Option A: Using AWS CLI**
```bash
# Set manifest.json MIME type
aws s3 cp s3://my-vegetarian-cookbook/manifest.json \
  s3://my-vegetarian-cookbook/manifest.json \
  --metadata-directive REPLACE \
  --content-type "application/manifest+json" \
  --acl public-read

# Set service worker MIME type
aws s3 cp s3://my-vegetarian-cookbook/sw.js \
  s3://my-vegetarian-cookbook/sw.js \
  --metadata-directive REPLACE \
  --content-type "application/javascript" \
  --acl public-read
```

**Option B: Using S3 Console**
1. Go to your bucket
2. Find `manifest.json`
3. Click → Actions → Edit metadata
4. Change Content-Type to: `application/manifest+json`
5. Repeat for `sw.js` → `application/javascript`

#### Step 4: Create CloudFront Distribution
```bash
# In AWS Console:
1. Go to CloudFront
2. Create Distribution
3. Origin Domain: Select your S3 bucket
4. Viewer Protocol Policy: Redirect HTTP to HTTPS
5. Default Root Object: index.html
6. Create Distribution
```

#### Step 5: Add Custom Domain (Optional but Recommended)
```bash
1. In CloudFront, add CNAME (e.g., cookbook.yoursite.com)
2. Get SSL certificate from ACM
3. Update DNS (Route53 or your provider)
4. Point to CloudFront distribution
```

**Result:** Your cookbook will be at `https://cookbook.yoursite.com` and the PWA name will show correctly!

---

### Option 2: S3 Only (Quick but Limited)

If you just want to test quickly:

#### Step 1: Upload Files
```bash
cd deploy
aws s3 sync . s3://your-bucket-name --acl public-read
```

#### Step 2: Enable Website Hosting
```bash
# In S3 Console:
1. Bucket → Properties → Static website hosting
2. Enable
3. Index document: index.html
```

#### Step 3: Fix MIME Types (Same as above)

**Limitations:**
- ⚠️ URL will be `bucket-name.s3-website-region.amazonaws.com`
- ⚠️ No HTTPS by default
- ⚠️ PWA might not install properly without HTTPS
- ✅ But with the manifest fix, the name should show correctly!

---

## 🔧 Additional S3 Configuration

### Bucket Policy (Make Everything Public)
Add this bucket policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```

### CORS Configuration (If Using Custom Domain)
Add this CORS policy:

```json
[
  {
    "AllowedHeaders": ["*"],
    "AllowedMethods": ["GET", "HEAD"],
    "AllowedOrigins": ["*"],
    "ExposeHeaders": []
  }
]
```

---

## 🎯 Testing After Deployment

### Test Checklist:
1. ✅ Open your S3/CloudFront URL
2. ✅ Check browser console for errors
3. ✅ Try "Add to Home Screen"
4. ✅ Verify app name shows as "Vegetarian Cookbook" (not AWS)
5. ✅ Test offline functionality
6. ✅ Check on mobile device

### Debug Commands:
```javascript
// In browser console:

// Check manifest is loaded
fetch('/manifest.json')
  .then(r => r.json())
  .then(console.log)

// Check service worker
navigator.serviceWorker.getRegistration()
  .then(console.log)

// Check if running as PWA
console.log('Standalone:', window.matchMedia('(display-mode: standalone)').matches)
```

---

## 🚨 Common Issues & Solutions

### Issue 1: Shows "aws.amazon.com" Instead of App Name
**Cause:** Manifest using absolute paths  
**Solution:** ✅ Already fixed! Regenerate with updated script

### Issue 2: "Add to Home Screen" Not Appearing
**Causes:**
- Not using HTTPS
- Manifest not loading
- Wrong MIME type
- Missing icons

**Solutions:**
```bash
# 1. Ensure HTTPS (use CloudFront)
# 2. Check manifest loads:
curl -I https://your-url/manifest.json
# Should show: content-type: application/manifest+json

# 3. Verify icons exist:
curl -I https://your-url/icon-192.png
curl -I https://your-url/icon-512.png
```

### Issue 3: Service Worker Not Registering
**Cause:** Wrong MIME type or not HTTPS  
**Solution:**
```bash
# Fix MIME type
aws s3 cp s3://bucket/sw.js s3://bucket/sw.js \
  --content-type "application/javascript" \
  --metadata-directive REPLACE
```

### Issue 4: App Name Still Wrong After Fix
**Solutions:**
1. Clear browser cache
2. Uninstall old PWA version
3. Re-add to home screen
4. Wait 5 minutes for S3/CloudFront cache

---

## 🎯 Recommended AWS Architecture

### Best Setup for Production:

```
User
  ↓
Route 53 (DNS)
  ↓
CloudFront (CDN + HTTPS)
  ↓
S3 Bucket (Static files)
```

**Benefits:**
- ✅ HTTPS (required for PWA)
- ✅ Fast (CDN caching)
- ✅ Custom domain
- ✅ Correct PWA behavior
- ✅ Cheap (~$1-5/month)

**Cost Estimate:**
- S3 storage: ~$0.023/GB/month
- CloudFront: ~$0.085/GB data transfer
- Route 53: ~$0.50/month per hosted zone
- **Total for small cookbook:** ~$1-3/month

---

## 🆚 Alternative Hosting (If S3 Issues Persist)

If you're still having issues with S3, try these alternatives:

### Option 1: Netlify (EASIEST!)
```bash
# Drag and drop deploy/ folder
# Or use CLI:
npm install -g netlify-cli
cd deploy
netlify deploy --prod
```
- ✅ Free tier
- ✅ HTTPS automatic
- ✅ Custom domain free
- ✅ No configuration needed
- ✅ Perfect PWA support

### Option 2: Vercel
```bash
npm install -g vercel
cd deploy
vercel --prod
```
- ✅ Free tier
- ✅ HTTPS automatic
- ✅ Great performance
- ✅ No issues

### Option 3: GitHub Pages
```bash
# Push deploy/ folder to GitHub
# Enable Pages in settings
```
- ✅ Free
- ✅ HTTPS automatic
- ✅ Easy setup
- ✅ Works great

### Option 4: Firebase Hosting
```bash
npm install -g firebase-tools
firebase init hosting
firebase deploy
```
- ✅ Free tier (10GB/month)
- ✅ Great PWA support
- ✅ Fast CDN

---

## 📋 Quick Deployment Comparison

| Platform | Difficulty | Cost | PWA Support | HTTPS | Best For |
|----------|-----------|------|-------------|-------|----------|
| **Netlify** | ⭐ Easy | Free | ✅ Perfect | ✅ Auto | **Recommended!** |
| **Vercel** | ⭐ Easy | Free | ✅ Perfect | ✅ Auto | Great choice |
| **GitHub Pages** | ⭐⭐ Medium | Free | ✅ Good | ✅ Auto | Simple projects |
| **S3 + CloudFront** | ⭐⭐⭐ Hard | ~$1-3/mo | ✅ Good* | ✅ Manual | AWS users |
| **S3 Only** | ⭐⭐ Medium | ~$0.50/mo | ⚠️ Limited | ❌ No | Testing only |
| **Firebase** | ⭐⭐ Medium | Free | ✅ Perfect | ✅ Auto | Google users |

*With the manifest fix I applied

---

## 🔄 Re-deploying After Fix

### If You Already Deployed to S3:

1. **Regenerate your cookbook:**
```bash
python cookbook_generator.py
```

2. **Upload the new manifest.json:**
```bash
aws s3 cp deploy/manifest.json s3://your-bucket/ \
  --content-type "application/manifest+json" \
  --acl public-read
```

3. **Clear CloudFront cache (if using):**
```bash
# In CloudFront Console:
# Distribution → Invalidations → Create Invalidation
# Path: /manifest.json
```

4. **Test:**
- Clear browser cache
- Uninstall old PWA
- Visit site again
- Add to home screen
- Should now show "Vegetarian Cookbook"! ✅

---

## 🎓 Understanding the Fix

### What Changed:

**Before (Caused AWS Issue):**
```json
{
  "start_url": "/",
  "scope": "/"
}
```
This made the browser think the app starts at the root of `aws.amazon.com`

**After (Fixed):**
```json
{
  "start_url": "./",
  "scope": "./"
}
```
This makes the app start at the current location, regardless of domain!

### Why Relative Paths Work:
- Works on localhost
- Works on S3 URLs
- Works on custom domains
- Works on subdirectories
- Universal solution!

---

## 🎉 Summary

### The Problem:
AWS S3 URLs caused PWA to show "aws.amazon.com" as app name

### The Solution:
✅ Updated manifest.json to use relative paths (`./`)

### Best Deployment Strategy:
1. **For ease:** Use Netlify (drag & drop)
2. **For AWS:** Use S3 + CloudFront + custom domain
3. **For testing:** S3 static hosting (with manifest fix)

### Your Next Steps:
1. Regenerate: `python cookbook_generator.py`
2. Deploy to preferred platform
3. Test "Add to Home Screen"
4. Should show "Vegetarian Cookbook" now! ✅

---

**The manifest is now fixed! Try Netlify for zero-hassle deployment! 🚀**
