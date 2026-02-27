# Deploy Cloud Certified Support to GitHub → Azure

## 🎯 CORRECT WORKFLOW

**February 27, 2026 - Professional Deployment**

1. ✅ Push code to GitHub (version control + backup)
2. ✅ Deploy from GitHub to Azure (professional workflow)
3. ✅ Show Microsoft you're a real developer

---

## STEP 1: Push to GitHub (15 minutes)

### 1A: Initialize Git (if not done)

```powershell
cd 'c:\Users\Woody\OneDrive - CLOUD AND SECURE LIMITED\Documents\Github\Repositories\cloudcertifiedsupport. com'

# Initialize git
git init

# Configure git (if not already done)
git config user.name "Gregory Woodruff"
git config user.email "gregory.woodruff@cloudcertifiedsupport.com"
```

### 1B: Add and Commit All Files

```powershell
# Add all files (respects .gitignore)
git add .

# Check what's being committed
git status

# Commit
git commit -m "Initial commit: Cloud Certified Support Inc website ready for Azure deployment"
```

### 1C: Create GitHub Repository

**Option A: Via GitHub Website (Recommended)**

1. Go to [https://github.com/new](https://github.com/new)
2. Repository name: `cloudcertifiedsupport.com`
3. Description: `Professional website for Cloud Certified Support Inc - Microsoft Azure consulting firm`
4. **Public** (so Microsoft can verify it's real)
5. **Do NOT initialize with README** (we already have code)
6. Click **"Create repository"**

**Option B: Via GitHub CLI (Faster if you have it)**

```powershell
gh repo create cloudcertifiedsupport.com --public --description "Cloud Certified Support Inc - Microsoft Azure Consulting Website" --source=.
```

### 1D: Push to GitHub

After creating the repo on GitHub, connect and push:

```powershell
# Add GitHub as remote (replace YOUR-USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR-USERNAME/cloudcertifiedsupport.com.git

# Push code
git branch -M main
git push -u origin main
```

**Expected output:**
```
Enumerating objects: 45, done.
Counting objects: 100% (45/45), done.
Delta compression using up to 8 threads
Compressing objects: 100% (38/38), done.
Writing objects: 100% (45/45), 12.34 KiB | 1.54 MiB/s, done.
Total 45 (delta 5), reused 0 (delta 0), pack-reused 0
To https://github.com/YOUR-USERNAME/cloudcertifiedsupport.com.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

✅ **Code is now on GitHub! Professional developer status achieved.**

---

## STEP 2: Deploy from GitHub to Azure (20 minutes)

Now that code is on GitHub, deploy to Azure with continuous deployment:

### 2A: Create Azure Web App

```powershell
# Login to Azure
az login

# Create resource group
az group create --name cloudcertifiedsupport-rg --location eastus

# Create App Service Plan
az appservice plan create `
  --name cloudcertifiedsupport-plan `
  --resource-group cloudcertifiedsupport-rg `
  --sku B1 `
  --is-linux

# Create Web App
az webapp create `
  --resource-group cloudcertifiedsupport-rg `
  --plan cloudcertifiedsupport-plan `
  --name cloudcertifiedsupport `
  --runtime "PYTHON:3.11"
```

### 2B: Connect Azure to GitHub (Continuous Deployment)

**Option 1: Via Azure Portal (Recommended - Visual)**

1. Go to [Azure Portal](https://portal.azure.com)
2. Navigate to your **cloudcertifiedsupport** web app
3. Go to **Deployment** → **Deployment Center**
4. **Source:** GitHub
5. Click **Authorize** (connects to your GitHub account)
6. **Organization:** Your GitHub username
7. **Repository:** cloudcertifiedsupport.com
8. **Branch:** main
9. Click **Save**

✅ Azure will now auto-deploy from GitHub whenever you push!

**Option 2: Via Azure CLI**

```powershell
# Get your GitHub username
$githubUser = "YOUR-GITHUB-USERNAME"

# Configure continuous deployment from GitHub
az webapp deployment source config `
  --name cloudcertifiedsupport `
  --resource-group cloudcertifiedsupport-rg `
  --repo-url "https://github.com/$githubUser/cloudcertifiedsupport.com" `
  --branch main `
  --manual-integration
```

### 2C: Configure Startup Command

```powershell
az webapp config set `
  --resource-group cloudcertifiedsupport-rg `
  --name cloudcertifiedsupport `
  --startup-file "startup.sh"
```

### 2D: Set Environment Variables

```powershell
# Generate secret key first
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Copy the output and use it below (replace YOUR_SECRET_KEY_HERE):
az webapp config appsettings set `
  --resource-group cloudcertifiedsupport-rg `
  --name cloudcertifiedsupport `
  --settings `
    DJANGO_SECRET_KEY="YOUR_SECRET_KEY_HERE" `
    DJANGO_DEBUG="False" `
    DJANGO_ALLOWED_HOSTS="cloudcertifiedsupport.com,cloudcertifiedsupport.azurewebsites.net,www.cloudcertifiedsupport.com" `
    SCM_DO_BUILD_DURING_DEPLOYMENT="true" `
    WEBSITE_HTTPLOGGING_RETENTION_DAYS="7"
```

### 2E: Verify Deployment

```powershell
# Open in browser
az webapp browse --name cloudcertifiedsupport --resource-group cloudcertifiedsupport-rg
```

You should see your site at: `https://cloudcertifiedsupport.azurewebsites.net`

If errors, check logs:
```powershell
az webapp log tail --name cloudcertifiedsupport --resource-group cloudcertifiedsupport-rg
```

---

## STEP 3: Point Custom Domain (10 minutes)

### 3A: Get Azure IP Address

```powershell
az webapp show `
  --name cloudcertifiedsupport `
  --resource-group cloudcertifiedsupport-rg `
  --query defaultHostName -o tsv
```

### 3B: Configure DNS (Your Domain Registrar)

Go to where you bought cloudcertifiedsupport.com (GoDaddy, Namecheap, etc.):

**Add CNAME Record:**
- **Type:** CNAME
- **Host:** `www`
- **Points to:** `cloudcertifiedsupport.azurewebsites.net`
- **TTL:** 3600 (1 hour)

**Add CNAME for root (if supported):**
- **Type:** CNAME or ALIAS
- **Host:** `@` or `cloudcertifiedsupport.com`
- **Points to:** `cloudcertifiedsupport.azurewebsites.net`
- **TTL:** 3600

*(If your registrar doesn't support CNAME for root, use A record with IP from Azure)*

### 3C: Add Custom Domain in Azure

**Via Azure Portal:**
1. Go to **cloudcertifiedsupport** web app
2. **Settings** → **Custom domains**
3. Click **+ Add custom domain**
4. Enter: `cloudcertifiedsupport.com`
5. Click **Validate**
6. Once validated, click **Add**
7. Repeat for `www.cloudcertifiedsupport.com`

**Via CLI:**
```powershell
# Add custom domain
az webapp config hostname add `
  --hostname cloudcertifiedsupport.com `
  --resource-group cloudcertifiedsupport-rg `
  --webapp-name cloudcertifiedsupport

az webapp config hostname add `
  --hostname www.cloudcertifiedsupport.com `
  --resource-group cloudcertifiedsupport-rg `
  --webapp-name cloudcertifiedsupport
```

### 3D: Enable HTTPS (FREE SSL Certificate)

**Via Azure Portal:**
1. **Custom domains** → Next to your domain
2. Click **Add binding**
3. **TLS/SSL cert:** App Service Managed Certificate (FREE)
4. **TLS/SSL type:** SNI SSL
5. Click **Add binding**
6. Wait 5-10 minutes

**Via CLI:**
```powershell
az webapp config ssl bind `
  --name cloudcertifiedsupport `
  --resource-group cloudcertifiedsupport-rg `
  --certificate-thumbprint auto `
  --ssl-type SNI
```

---

## STEP 4: Future Updates (2 minutes each)

**Now that GitHub → Azure is connected, deploying updates is EASY:**

```powershell
# Make changes to code
# ...edit files...

# Commit and push
git add .
git commit -m "Added Bass Pro Shops to portfolio"
git push origin main
```

✅ **Azure automatically deploys within 2-3 minutes!**

No need to run `az webapp up` again. Just push to GitHub.

---

## ✅ BENEFITS OF THIS WORKFLOW

**vs. Direct Azure Deployment:**

| Feature | Direct Deploy | GitHub → Azure |
|---------|---------------|----------------|
| Version control | ❌ No | ✅ Full history |
| Backup | ❌ No | ✅ GitHub backup |
| Collaboration | ❌ Hard | ✅ Easy (PRs, branches) |
| Auto-deploy | ❌ Manual | ✅ Push = deploy |
| Rollback | ❌ Hard | ✅ Revert commit |
| Professional | ❌ Amateur | ✅ Industry standard |
| Microsoft approval | ❌ Questionable | ✅ Looks legit |

---

## 📊 COMPLETE CHECKLIST

**GitHub Setup (First Time Only):**
- [ ] `git init` in project folder
- [ ] `git add .` to stage files
- [ ] `git commit -m "Initial commit"`
- [ ] Create GitHub repo (github.com/new)
- [ ] `git remote add origin ...`
- [ ] `git push -u origin main`
- ✅ Code on GitHub!

**Azure Deployment (First Time Only):**
- [ ] `az login`
- [ ] Create resource group
- [ ] Create App Service plan
- [ ] Create Web App
- [ ] Connect GitHub to Azure (Deployment Center)
- [ ] Set startup command
- [ ] Set environment variables
- [ ] Verify site loads
- ✅ Site on Azure!

**Domain Setup (One Time):**
- [ ] Add CNAME in domain registrar
- [ ] Add custom domain in Azure
- [ ] Enable free SSL certificate
- [ ] Wait for DNS (1-24 hours)
- ✅ cloudcertifiedsupport.com LIVE!

**Future Updates (Every Time):**
- [ ] Edit code
- [ ] `git add .`
- [ ] `git commit -m "Description"`
- [ ] `git push origin main`
- [ ] Wait 2-3 minutes
- ✅ Changes live automatically!

---

## 💰 COST

**Monthly Azure Costs:**
- App Service Plan (B1): **$13/month**
- Bandwidth (low traffic): **$1-2/month**
- SSL Certificate: **FREE** (App Service Managed)
- **Total: ~$15/month**

**GitHub:**
- Public repo: **FREE**
- Private repos: **FREE** (unlimited)

---

## 📧 EMAIL MICROSOFT AFTER DEPLOYMENT

```
Subject: Cloud Certified Support Inc - GitHub Repo + Live Azure Site

Dear Microsoft Vetting Operations,

I'm writing to confirm that Cloud Certified Support Inc has completed website deployment with professional development workflow:

✅ **GitHub Repository:** https://github.com/YOUR-USERNAME/cloudcertifiedsupport.com (public)
✅ **Live Website:** https://cloudcertifiedsupport.com (Azure-hosted)
✅ **Staging URL:** https://cloudcertifiedsupport.azurewebsites.net

**Updated Documents:**
- Domain renewal: cloudcertifiedsupport.com (expires February 2029)
- February 2026 utility bill (service through April 2026)
- February 2026 bank statement

Our website uses industry-standard deployment (GitHub → Azure) demonstrating active software development capabilities. The repository shows commit history, professional code structure, and production-ready Django application.

Please complete the verification for our Microsoft Partner status.

Best regards,
Gregory Woodruff
Founder & CEO
Cloud Certified Support Inc
gregory.woodruff@cloudcertifiedsupport.com
```

---

## 🚀 QUICK START COMMANDS

**Copy-paste this entire block (replace YOUR-GITHUB-USERNAME):**

```powershell
# Navigate to project
cd 'c:\Users\Woody\OneDrive - CLOUD AND SECURE LIMITED\Documents\Github\Repositories\cloudcertifiedsupport. com'

# Git setup
git init
git config user.name "Gregory Woodruff"
git config user.email "gregory.woodruff@cloudcertifiedsupport.com"
git add .
git commit -m "Initial commit: Professional Azure consulting website"

# Create GitHub repo via browser first: https://github.com/new
# Name it: cloudcertifiedsupport.com
# Then run (replace YOUR-GITHUB-USERNAME):

git remote add origin https://github.com/YOUR-GITHUB-USERNAME/cloudcertifiedsupport.com.git
git branch -M main
git push -u origin main

# Azure deployment
az login
az group create --name cloudcertifiedsupport-rg --location eastus
az appservice plan create --name cloudcertifiedsupport-plan --resource-group cloudcertifiedsupport-rg --sku B1 --is-linux
az webapp create --resource-group cloudcertifiedsupport-rg --plan cloudcertifiedsupport-plan --name cloudcertifiedsupport --runtime "PYTHON:3.11"
az webapp config set --resource-group cloudcertifiedsupport-rg --name cloudcertifiedsupport --startup-file "startup.sh"

# Generate secret (save output):
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Set environment variables (replace YOUR_SECRET_KEY with output above):
az webapp config appsettings set --resource-group cloudcertifiedsupport-rg --name cloudcertifiedsupport --settings DJANGO_SECRET_KEY="YOUR_SECRET_KEY" DJANGO_DEBUG="False" DJANGO_ALLOWED_HOSTS="cloudcertifiedsupport.com,cloudcertifiedsupport.azurewebsites.net,www.cloudcertifiedsupport.com" SCM_DO_BUILD_DURING_DEPLOYMENT="true"

# Open site
az webapp browse --name cloudcertifiedsupport --resource-group cloudcertifiedsupport-rg

# Connect GitHub in Azure Portal: https://portal.azure.com
# Go to cloudcertifiedsupport → Deployment Center → GitHub
```

**DONE! Site deployed with professional workflow.**

---

**Gregory - THIS is how real developers work. Microsoft will see your GitHub commits and know you're legit.**
