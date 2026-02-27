# CloudCertifiedSupport.com - Action Plan
## Next Steps for Development

**Last Updated:** February 26, 2026  
**Status:** Database ready, base templates created, needs content and remaining templates

---

## Current Status ✅

**Completed:**
- ✅ Django 5.0.1 project structure created
- ✅ 5 content models built (Page, Service, PortfolioItem, BlogPost, ContactSubmission)
- ✅ Django admin fully configured with custom branding
- ✅ Database migrations applied (SQLite local)
- ✅ Superuser created (admin / CloudCertified2026!)
- ✅ 3 templates created (base.html, home.html, contact.html)
- ✅ High contrast toggle button added
- ✅ Development server running on port 8001

**Current URLs:**
- **Local site:** http://localhost:8001/
- **Django admin:** http://localhost:8001/admin/
- **Username:** admin
- **Password:** CloudCertified2026!

---

## Phase 1: Add Initial Content (PRIORITY 1) 🎯

**Why First:** We need content to test the templates and see how the site looks with real data.

**What Woody Should Do:**

### 1. Log into Django Admin
Visit http://localhost:8001/admin/ and log in.

### 2. Create 3-5 Services

Click **"Services"** → **"Add Service"**

**Suggested services:**

1. **Azure Consulting**
   - Category: Azure Services
   - Short description: "Expert guidance for Azure architecture, migrations, and optimization"
   - Is Featured: ✓ (check this - it will appear on homepage)
   - Is Active: ✓

2. **Cloud Migration**
   - Category: Migration Services
   - Short description: "Seamless migration of applications and data to Microsoft Azure"
   - Is Featured: ✓
   - Is Active: ✓

3. **Microsoft 365 Integration**
   - Category: Microsoft 365
   - Short description: "Complete Microsoft 365 setup, migration, and integration services"
   - Is Featured: ✓
   - Is Active: ✓

4. **Healthcare Solutions**
   - Category: Custom Development
   - Short description: "HIPAA-compliant Azure applications for healthcare organizations"
   - Is Active: ✓

5. **Technical Support**
   - Category: Support & Training
   - Short description: "Ongoing Azure support and troubleshooting for your team"
   - Is Active: ✓

### 3. Create 2-4 Portfolio Items

Click **"Portfolio Items"** → **"Add Portfolio Item"**

**Required projects:**

1. **BrentwoodBlvd Healthcare Analytics**
   - Title: "BrentwoodBlvd Healthcare Analytics Platform"
   - Project Type: Healthcare
   - Client Name: [Leave blank or "Confidential Healthcare Client"]
   - Short description: "Azure Functions-based healthcare analytics platform serving 5,000+ users"
   - Technologies Used: "Azure Functions, Python, Django, PostgreSQL, Azure Static Web Apps, AI/ML"
   - Project URL: https://brentwoodblvd.com
   - Is Featured: ✓ (homepage display)
   - Is Published: ✓

2. **YouBetYourAzure Educational Platform**
   - Title: "YouBetYourAzure - Azure Education Initiative"
   - Project Type: Education
   - Short description: "Educational platform teaching Microsoft Azure concepts to students and professionals"
   - Technologies Used: "Azure Static Web Apps, GitHub Pages, JavaScript, HTML/CSS"
   - Project URL: https://youbetyourazure.com
   - Is Featured: ✓
   - Is Published: ✓

3. **MintonHomes Business Portal** (In Development)
   - Title: "MintonHomes LLC Business Management Portal"
   - Project Type: Business Applications
   - Short description: "Comprehensive business portal with Microsoft 365 integration"
   - Technologies Used: "Django, Azure App Service, PostgreSQL, Microsoft Graph API, Microsoft 365"
   - Is Featured: ✓ (show as active project)
   - Is Published: ✓

4. **Cloud and Secure Limited Portal**
   - Title: "Internal Business Management Portal"
   - Project Type: Business Applications
   - Short description: "Custom Django portal for domain management, ideas tracking, and business operations"
   - Technologies Used: "Django, Azure PostgreSQL, Azure Static Web Apps, Python"
   - Project URL: https://portal.cloudandsecurelimited.com
   - Is Published: ✓

### 4. Create 1-2 Custom Pages (Optional)

Click **"Pages"** → **"Add Page"**

1. **About Page**
   - Title: "About Cloud Certified Support Inc"
   - Slug: about
   - Content: Write about 30 years of experience, Missouri corporation, etc.
   - Is Published: ✓
   - Show in Navigation: ✓

**Time Estimate:** 30-45 minutes

---

## Phase 2: Create Remaining Templates (PRIORITY 2) 📝

**What Copilot Should Do:** Create 9 remaining templates

**Templates Needed:**

1. ✅ `base.html` - DONE
2. ✅ `home.html` - DONE  
3. ✅ `contact.html` - DONE
4. ⬜ `services.html` - Services list page (grouped by category)
5. ⬜ `service_detail.html` - Individual service page
6. ⬜ `portfolio.html` - Portfolio grid with filtering
7. ⬜ `portfolio_detail.html` - Individual project case study
8. ⬜ `education.html` - Education hub (YouBetYourAzure showcase)
9. ⬜ `healthcare.html` - Healthcare solutions (BrentwoodBlvd showcase)
10. ⬜ `blog.html` - Blog post list
11. ⬜ `blog_post.html` - Individual blog post
12. ⬜ `page_detail.html` - Generic page template

**Time Estimate:** 1-2 hours (Copilot)

---

## Phase 3: Local Testing (PRIORITY 3) 🧪

**What Woody Should Do:**

1. Test all pages in high contrast mode
2. Use toggle button to preview normal colors
3. Test contact form submission
4. Verify all links work
5. Check responsive design on mobile (browser dev tools)
6. Test navigation between pages

**Time Estimate:** 30 minutes

---

## Phase 4: Azure PostgreSQL Setup (PRIORITY 4) ☁️

**What Woody Should Do:**

### Create PostgreSQL Database

Open PowerShell in Azure subscription:

```powershell
# Login to Azure
az login

# Create resource group
az group create --name cloudcertifiedsupport-rg --location centralus

# Create PostgreSQL server
az postgres flexible-server create `
    --name cloudcertifiedsupport-db `
    --resource-group cloudcertifiedsupport-rg `
    --location centralus `
    --admin-user ccadmin `
    --admin-password 'YourSecurePassword123!' `
    --sku-name Standard_B1ms `
    --tier Burstable `
    --storage-size 32

# Create database
az postgres flexible-server db create `
    --resource-group cloudcertifiedsupport-rg `
    --server-name cloudcertifiedsupport-db `
    --database-name cloudcertifiedsupport

# Configure firewall for Azure services
az postgres flexible-server firewall-rule create `
    --resource-group cloudcertifiedsupport-rg `
    --name cloudcertifiedsupport-db `
    --rule-name AllowAzureServices `
    --start-ip-address 0.0.0.0 `
    --end-ip-address 0.0.0.0
```

### Update Django Settings

Edit `settings.py` to use PostgreSQL:

```python
# Uncomment PostgreSQL configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'cloudcertifiedsupport'),
        'USER': os.environ.get('DB_USER', 'ccadmin'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', 'cloudcertifiedsupport-db.postgres.database.azure.com'),
        'PORT': '5432',
    }
}
```

### Create `.env` file

```
DB_NAME=cloudcertifiedsupport
DB_USER=ccadmin
DB_PASSWORD=YourSecurePassword123!
DB_HOST=cloudcertifiedsupport-db.postgres.database.azure.com
SECRET_KEY=your-production-secret-key
DEBUG=False
```

### Run Migrations on Azure Database

```powershell
python manage.py migrate
python manage.py createsuperuser
```

**Time Estimate:** 30 minutes  
**Cost:** ~$20-30/month for Burstable tier PostgreSQL

---

## Phase 5: Azure Web Apps Deployment (PRIORITY 5) 🚀

**What Woody Should Do:**

### Deploy to Azure App Service

```powershell
# Create App Service
az webapp up `
    --resource-group cloudcertifiedsupport-rg `
    --name cloudcertifiedsupport `
    --runtime "PYTHON:3.11" `
    --sku B1 `
    --location centralus
```

### Configure Environment Variables

```powershell
az webapp config appsettings set `
    --resource-group cloudcertifiedsupport-rg `
    --name cloudcertifiedsupport `
    --settings `
        DB_NAME=cloudcertifiedsupport `
        DB_USER=ccadmin `
        DB_PASSWORD=YourSecurePassword123! `
        DB_HOST=cloudcertifiedsupport-db.postgres.database.azure.com `
        SECRET_KEY=your-production-secret-key `
        DEBUG=False `
        ALLOWED_HOSTS=cloudcertifiedsupport.azurewebsites.net,cloudcertifiedsupport.com
```

### Configure Static Files

Add to Azure App Service configuration:

```powershell
az webapp config appsettings set `
    --resource-group cloudcertifiedsupport-rg `
    --name cloudcertifiedsupport `
    --settings `
        DISABLE_COLLECTSTATIC=0
```

**Time Estimate:** 45 minutes  
**Cost:** ~$13/month for B1 tier App Service

---

## Phase 6: Custom Domain & SSL (PRIORITY 6) 🔒

**What Woody Should Do:**

1. Add custom domain in Azure Portal:
   - Go to App Service → Custom domains
   - Add: cloudcertifiedsupport.com

2. Update DNS at Hover:
   - Add CNAME: cloudcertifiedsupport.com → cloudcertifiedsupport.azurewebsites.net
   - Or A record pointing to App Service IP

3. Enable SSL:
   - Azure Portal → TLS/SSL settings
   - Add managed certificate (free)
   - Bind to cloudcertifiedsupport.com

**Time Estimate:** 15 minutes  
**Cost:** Free (Azure-managed certificate)

---

## Phase 7: SEO & Content (PRIORITY 7) 📈

**Optional - Future Enhancement:**

1. Write 3-5 blog posts
2. Create sitemap.xml
3. Add Google Analytics
4. Submit to Google Search Console
5. Add schema.org markup
6. Optimize images

---

## Recommended Order of Execution

**TODAY (February 26, 2026):**
1. ✅ Woody: Add content via Django admin (30-45 min)
2. ✅ Copilot: Create remaining templates (1-2 hours)
3. ✅ Woody: Test all pages locally (30 min)

**NEXT SESSION:**
4. ⬜ Woody: Set up Azure PostgreSQL (30 min, ~$20/month)
5. ⬜ Woody: Deploy to Azure App Service (45 min, ~$13/month)
6. ⬜ Woody: Configure custom domain (15 min)

**Total Time:** ~4-5 hours  
**Total Cost:** ~$33/month (PostgreSQL + App Service)

---

## Copilot Ready to Proceed With:

**Option A: Continue with Phase 2** (Create remaining templates)
- I can create all 9 templates right now while you add content to admin
- We'll see the site come alive with real data in the templates

**Option B: Azure Setup Assistance** (Phase 4)
- I can walk you through PostgreSQL creation step-by-step
- We can test database connection before deployment

**Option C: Something Else**
- Let me know what you want to tackle first!

---

**What would you like to do next, Woody?**
