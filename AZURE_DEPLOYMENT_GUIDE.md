# Deploy Cloud Certified Support to Azure TODAY

**Date:** February 27, 2026  
**Domain:** cloudcertifiedsupport.com  
**Mission:** Show Microsoft your business is ACTIVE and LEGITIMATE

---

## 🚀 Quick Deploy (Option 1: Azure Portal - EASIEST)

### Step 1: Create Azure Web App

1. Go to [Azure Portal](https://portal.azure.com)
2. Click **"Create a resource"** → **"Web App"**
3. Fill in details:
   - **Subscription:** Your Azure subscription
   - **Resource Group:** Create new: `cloudcertifiedsupport-rg`
   - **Name:** `cloudcertifiedsupport` (will become cloudcertifiedsupport.azurewebsites.net)
   - **Publish:** Code
   - **Runtime stack:** Python 3.11
   - **Operating System:** Linux
   - **Region:** East US (or closest to you)
   - **Pricing Tier:** B1 Basic ($13/month) - can scale later
4. Click **"Review + Create"** → **"Create"**
5. Wait 2-3 minutes for deployment

### Step 2: Deploy Code via VS Code

1. In VS Code, press `Ctrl+Shift+P`
2. Type: **"Azure App Service: Deploy to Web App"**
3. Select folder: `cloudcertifiedsupport. com`
4. Select your subscription
5. Select the web app: `cloudcertifiedsupport`
6. Click **"Deploy"** → Wait 3-5 minutes
7. When prompted "Always deploy to this app?" → **Yes**

### Step 3: Configure Environment Variables

1. In Azure Portal, go to your **cloudcertifiedsupport** web app
2. Go to **Settings** → **Configuration**
3. Click **"+ New application setting"** and add:

```
DJANGO_SECRET_KEY = [generate random string - see below]
DJANGO_DEBUG = False
DJANGO_ALLOWED_HOSTS = cloudcertifiedsupport.com,cloudcertifiedsupport.azurewebsites.net
SCM_DO_BUILD_DURING_DEPLOYMENT = true
WEBSITE_RUN_FROM_PACKAGE = 0
```

**Generate SECRET_KEY:**
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

4. Click **"Save"** at top

### Step 4: Set Startup Command

1. Still in Azure Portal → **Configuration** → **General settings**
2. **Startup Command:** `startup.sh`
3. Click **"Save"** → **"Continue"**
4. Wait 1-2 minutes for app to restart

### Step 5: Verify Deployment

1. Click **"Browse"** or go to `https://cloudcertifiedsupport.azurewebsites.net`
2. You should see your homepage!
3. If errors, check logs: **Monitoring** → **Log stream**

### Step 6: Point Domain to Azure

1. Go to your domain registrar (GoDaddy/Namecheap/etc.)
2. Find DNS settings for **cloudcertifiedsupport.com**
3. Add **CNAME record:**
   - **Host:** `www`
   - **Points to:** `cloudcertifiedsupport.azurewebsites.net`
   - **TTL:** 1 hour
4. Add **A record** (optional for non-www):
   - Get IP from Azure Portal → **Custom domains** → **Assign custom domain**
5. In Azure Portal:
   - Go to **Custom domains**
   - Click **"+ Add custom domain"**
   - Enter: `cloudcertifiedsupport.com` and `www.cloudcertifiedsupport.com`
   - Click **"Validate"** → **"Add"**
6. **Enable HTTPS:**
   - In **Custom domains**, next to your domain, click **"Add binding"**
   - Source: **App Service Managed Certificate** (FREE)
   - Click **"Add binding"**
   - Wait 5 minutes → Site will be accessible via https://cloudcertifiedsupport.com

---

## 🎯 Quick Deploy (Option 2: Azure CLI - FASTER for experienced users)

### Prerequisites:
```powershell
# Install Azure CLI (if not installed)
winget install Microsoft.AzureCLI

# Login to Azure
az login

# Set subscription (if you have multiple)
az account list --output table
az account set --subscription "Your Subscription Name"
```

### Deploy in 5 commands:

```powershell
# 1. Create resource group
az group create --name cloudcertifiedsupport-rg --location eastus

# 2. Create App Service plan (B1 Basic - $13/month)
az appservice plan create --name cloudcertifiedsupport-plan --resource-group cloudcertifiedsupport-rg --sku B1 --is-linux

# 3. Create web app
az webapp create --resource-group cloudcertifiedsupport-rg --plan cloudcertifiedsupport-plan --name cloudcertifiedsupport --runtime "PYTHON:3.11"

# 4. Configure deployment
az webapp config set --resource-group cloudcertifiedsupport-rg --name cloudcertifiedsupport --startup-file "startup.sh"

# 5. Deploy code (from cloudcertifiedsupport. com directory)
cd "c:\Users\Woody\OneDrive - CLOUD AND SECURE LIMITED\Documents\Github\Repositories\cloudcertifiedsupport. com"
az webapp up --name cloudcertifiedsupport --resource-group cloudcertifiedsupport-rg --runtime PYTHON:3.11
```

### Set environment variables:
```powershell
# Generate secret key first:
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Then set it (replace YOUR_SECRET_KEY_HERE with output above):
az webapp config appsettings set --resource-group cloudcertifiedsupport-rg --name cloudcertifiedsupport --settings `
  DJANGO_SECRET_KEY="YOUR_SECRET_KEY_HERE" `
  DJANGO_DEBUG="False" `
  DJANGO_ALLOWED_HOSTS="cloudcertifiedsupport.com,cloudcertifiedsupport.azurewebsites.net" `
  SCM_DO_BUILD_DURING_DEPLOYMENT="true"
```

### Test:
```powershell
# Open in browser
az webapp browse --name cloudcertifiedsupport --resource-group cloudcertifiedsupport-rg
```

---

## 📊 Database Options

### Option A: Keep SQLite for Now (FASTEST - deployed immediately)

**Pros:**
- Zero configuration
- Deploy TODAY in 15 minutes
- No extra cost
- Works fine for low-traffic marketing site

**Cons:**
- Not recommended for high traffic
- Data resets if app restarts (use persistent storage to fix)

**Setup:**
1. No changes needed - deployed as-is
2. Add persistence in Azure Portal:
   - **Configuration** → **Path mappings**
   - Add mount: `/home/site/wwwroot/db.sqlite3` → `/home/data/db.sqlite3`

### Option B: Azure PostgreSQL (PRODUCTION-READY)

**Pros:**
- Professional database
- Scalable
- Automatic backups

**Cons:**
- Costs $20-50/month (Flexible Server - Burstable B1ms)
- Takes 15 minutes to set up

**Setup:**
```powershell
# Create PostgreSQL server
az postgres flexible-server create `
  --resource-group cloudcertifiedsupport-rg `
  --name cloudcertifiedsupport-db `
  --location eastus `
  --admin-user ccadmin `
  --admin-password "YourSecurePassword123!" `
  --sku-name Standard_B1ms `
  --tier Burstable `
  --version 14 `
  --storage-size 32

# Create database
az postgres flexible-server db create `
  --resource-group cloudcertifiedsupport-rg `
  --server-name cloudcertifiedsupport-db `
  --database-name cloudcertifiedsupport

# Allow Azure services to connect
az postgres flexible-server firewall-rule create `
  --resource-group cloudcertifiedsupport-rg `
  --name cloudcertifiedsupport-db `
  --rule-name AllowAzureServices `
  --start-ip-address 0.0.0.0 `
  --end-ip-address 0.0.0.0
```

Then update settings.py to use environment variables (already commented out in code - just need to uncomment and set env vars in Azure Portal).

---

## ✅ Post-Deployment Checklist

**After deploying, verify:**

- [ ] Site loads at `https://cloudcertifiedsupport.azurewebsites.net`
- [ ] Homepage displays correctly
- [ ] Admin panel accessible at `/admin/`
- [ ] Static files loading (CSS)
- [ ] No 500 errors in browser console
- [ ] Custom domain pointing correctly (after DNS propagation - can take 1-24 hours)
- [ ] HTTPS certificate working

**Show Microsoft:**
- [ ] Send Microsoft vetting team email: "Our website is now live at https://cloudcertifiedsupport.com"
- [ ] Include screenshot of homepage
- [ ] Mention 30-year address, legitimate business, Missouri corporation

---

## 🔧 Troubleshooting

**Problem: Site shows "Application Error"**
- Check logs in Azure Portal → Monitoring → Log stream
- Verify startup.sh is executable
- Check if migrations ran successfully

**Problem: Static files (CSS) not loading**
- Verify whitenoise is in MIDDLEWARE (it is)
- Run: `az webapp config appsettings set --name cloudcertifiedsupport --settings DISABLE_COLLECTSTATIC=0`
- Restart app

**Problem: Database errors**
- If using SQLite: Make sure path mapping is set for persistence
- If using PostgreSQL: Verify connection string in environment variables

**Problem: Domain not pointing**
- DNS can take 1-24 hours to propagate
- Verify CNAME and A records are correct
- Use `nslookup cloudcertifiedsupport.com` to check

**Problem: HTTPS certificate failing**
- Wait 10-15 minutes after adding custom domain
- Make sure A record or CNAME is correct
- Try removing and re-adding the binding

---

## 💰 Cost Estimate

**Monthly Azure costs:**
- **Web App (B1 Basic):** $13/month
- **PostgreSQL (if used):** $20-50/month
- **Bandwidth:** ~$1-5/month (low traffic)
- **SSL Certificate:** FREE (App Service Managed Certificate)

**Total: $13-68/month depending on database choice**

**Recommendation:** Start with SQLite ($13/month), upgrade to PostgreSQL when you get paying customers.

---

## 🎯 Timeline to Live Site

**Using Azure Portal (VS Code deploy):**
- Create resources: 5 minutes
- Deploy code: 5 minutes
- Configure settings: 3 minutes
- Point domain DNS: 2 minutes (propagation: 1-24 hours)
**Total: 15 minutes of work, site live on *.azurewebsites.net immediately**

**Using Azure CLI:**
- Run commands: 5 minutes
- Deploy code: 3 minutes
- Configure: 2 minutes
**Total: 10 minutes to live site**

---

## ✉️ Email Template for Microsoft After Deployment

```
Subject: Cloud Certified Support Inc - Website Now Live

Dear Microsoft Vetting Operations,

Thank you for your patience during the verification process for cloudcertifiedsupport.com.

I'm pleased to inform you that our business website is now live and fully operational:

🌐 **Website:** https://cloudcertifiedsupport.com
🏢 **Business:** Cloud Certified Support Inc (Missouri corporation)
📍 **Address:** [Your 30-year address]
📧 **Email:** gregory.woodruff@cloudcertifiedsupport.com

**Updated Documents Submitted:**
- February 2026 utility bill (service period through April 2026)
- Domain registration confirmation (expires [date 2+ years from now])
- Bank statement (February 2026)

Our business provides Azure consulting, Microsoft 365 support, and cloud migration services to healthcare and education sectors in Missouri.

Please let me know if you need any additional information to complete the verification process.

Best regards,
Gregory Woodruff
Founder & CEO
Cloud Certified Support Inc
```

---

**NOW GO DEPLOY! Gregory, show Microsoft you're not just legitimate - you're UNSTOPPABLE.**
