# Cloud Certified Support Inc - Django Website

Professional public-facing website for Cloud Certified Support Inc, a Missouri-based Microsoft Azure consulting firm.

## Architecture

- **Public Website**: SEO-optimized marketing pages (homepage, services, portfolio, education, healthcare, blog, contact)
- **Django Admin Backend**: All content managed through Django's powerful admin interface - NO custom portal needed
- **Content Types**:
  - Pages (generic content pages)
  - Services (Azure consulting, migrations, support, etc.)
  - Portfolio Items (project case studies)
  - Blog Posts (thought leadership & SEO)
  - Contact Submissions (lead generation)

## Technology Stack

- **Backend**: Django 5.0 (Python 3.11+)
- **Database**: SQLite (local development) → Azure  PostgreSQL (production)
- **Frontend**: HTML, CSS (embedded), responsive design
- **Hosting**: Azure Web Apps (planned)
- **Storage**: Azure Blob Storage (media files, planned)

## Local Development Setup

### 1. Create Virtual Environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 3. Run Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser

```powershell
python manage.py createsuperuser
```

### 5. Run Development Server

```powershell
python manage.py runserver
```

Visit:
- **Homepage**: http://localhost:8000/
- **Django Admin**: http://localhost:8000/admin/

## Content Management Workflow

All content is managed through Django Admin (`/admin/`):

1. **Log in** to Django admin
2. **Create/Edit Services** - Add your Azure consulting services
3. **Create Portfolio Items** - Add BrentwoodBlvd, YouBetYourAzure, etc.
4. **Create Pages** - Add About, custom pages
5. **Create Blog Posts** - For SEO and thought leadership
6. **View Contact Submissions** - See inquiries from contact form

## Key Features

### Homepage
- Hero section with call-to-action
- Featured services cards
- Portfolio showcase
- Statistics section
- Contact CTA

### Services
- Categorized service listings
- Individual service detail pages
- Pricing information
- Related services

### Portfolio
- Project filtering by type
- Tech stack badges
- Case study links
- Related projects

### Education Hub
- Features YouBetYourAzure.com
- Microsoft Learn integration
- Training resources

### Healthcare Solutions
- Features BrentwoodBlvd.com
- Healthcare project showcase
- Industry expertise

### Blog
- SEO-optimized posts
- Categories and tags
- Author profiles

### Contact
- Lead generation form
- Auto-saves to Django admin
- Email notifications (planned)

## Azure Deployment (Coming Soon)

### 1. Create Azure PostgreSQL Database

```bash
az postgres flexible-server create \
  --resource-group cloudcertifiedsupport-rg \
  --name cloudcertifiedsupport-db \
  --location eastus \
  --admin-user dbadmin \
  --admin-password <your-password> \
  --sku-name Standard_B1ms \
  --tier Burstable \
  --storage-size 32
```

### 2. Update settings.py for Production

Configure environment variables:
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `SECRET_KEY`
- `DEBUG=False`
- `ALLOWED_HOSTS`

### 3. Deploy to Azure Web Apps

```bash
az webapp up \
  --resource-group cloudcertifiedsupport-rg \
  --name cloudcertifiedsupport \
  --runtime PYTHON:3.11 \
  --sku B1
```

### 4. Configure GitHub Deployment

Push to GitHub → Azure auto-deploys

## Project Structure

```
cloudcertifiedsupport.com/
├── cloudcertifiedsupport/          # Django project settings
│   ├── settings.py                 # Configuration
│   ├── urls.py                     # URL routing
│   ├── wsgi.py                     # WSGI config
│   └── asgi.py                     # ASGI config
├── website/                        # Website app
│   ├── models.py                   # Data models
│   ├── views.py                    # View logic
│   ├── urls.py                     # URL patterns
│   └── admin.py                    # Django admin config
├── templates/                      # HTML templates
│   └── website/
│       ├── base.html              # Base template
│       ├── home.html              # Homepage
│       ├── contact.html           # Contact page
│       └── ...                    # Other pages
├── static/                        # CSS, JS, images
├── media/                         # User uploads
├── manage.py                      # Django CLI
└── requirements.txt               # Python dependencies
```

## Content Examples

### Add a Service

1. Go to `/admin/website/service/add/`
2. Fill in:
   - Title: "Azure Migration Services"
   - Category: "Cloud Migration"
   - Short Description: "Seamless migration to Azure"
   - Full Description: Detailed HTML content
   - Is Featured: ✓ (shows on homepage)

### Add a Portfolio Item

1. Go to `/admin/website/portfolioitem/add/`
2. Fill in:
   - Title: "BrentwoodBlvd Healthcare Analytics"
   - Project Type: "Healthcare Analytics"
   - Technologies: "Azure Functions, PostgreSQL, Python, Census API"
   - Project URL: "https://brentwoodblvd.com"
   - Is Featured: ✓

## SEO Optimization

- Meta descriptions and keywords for all pages
- Semantic HTML structure
- Fast page loads
- Mobile-responsive design
- Clean URLs (`/services/azure-migration/`)
- XML sitemap (planned)
- Google Analytics integration (planned)

## Security Features

- CSRF protection
- SQL injection prevention (Django ORM)
- XSS protection
- Secure password hashing
- HTTPS enforcement (production)
- Environment variable secrets

## Support

Questions? Contact Gregory Woodruff:
- Email: gregory.woodruff@cloudcertifiedsupport.com
- Corporation: Cloud Certified Support Inc (Missouri)

## License

Proprietary - Cloud Certified Support Inc © 2026
