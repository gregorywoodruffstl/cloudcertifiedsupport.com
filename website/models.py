from django.db import models
from django.utils.text import slugify


class Page(models.Model):
    """Content pages (About, Services, etc.) managed via Django admin"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField(help_text="Main page content (HTML allowed)")
    meta_description = models.CharField(max_length=160, blank=True, help_text="SEO meta description")
    meta_keywords = models.CharField(max_length=255, blank=True, help_text="SEO keywords (comma-separated)")
    is_published = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    show_in_navigation = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class Service(models.Model):
    """Services offered by Cloud Certified Support"""
    CATEGORY_CHOICES = [
        ('AZURE', 'Azure Consulting'),
        ('M365', 'Microsoft 365'),
        ('MIGRATION', 'Cloud Migration'),
        ('SUPPORT', 'Technical Support'),
        ('TRAINING', 'Training & Education'),
        ('CUSTOM', 'Custom Development'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='AZURE')
    short_description = models.CharField(max_length=255, help_text="Brief description for cards/listings")
    full_description = models.TextField(help_text="Detailed service description (HTML allowed)")
    icon_class = models.CharField(max_length=100, blank=True, help_text="CSS icon class (e.g., 'fas fa-cloud')")
    pricing_info = models.CharField(max_length=200, blank=True, help_text="e.g., 'Starting at $150/hour'")
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"


class PortfolioItem(models.Model):
    """Portfolio projects and case studies"""
    PROJECT_TYPE_CHOICES = [
        ('HEALTHCARE', 'Healthcare Analytics'),
        ('EDUCATION', 'Educational Platform'),
        ('BUSINESS', 'Business Application'),
        ('MIGRATION', 'Cloud Migration'),
        ('INTEGRATION', 'System Integration'),
        ('OTHER', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPE_CHOICES, default='BUSINESS')
    client_name = models.CharField(max_length=200, blank=True, help_text="Can be left blank for confidentiality")
    short_description = models.CharField(max_length=255)
    full_description = models.TextField(help_text="Detailed project description (HTML allowed)")
    technologies_used = models.CharField(max_length=500, help_text="Comma-separated (Azure, Django, PostgreSQL, etc.)")
    project_url = models.URLField(blank=True, help_text="Live project URL if public")
    case_study_url = models.URLField(blank=True, help_text="Link to detailed case study")
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-completion_date', 'order']
        verbose_name = 'Portfolio Item'
        verbose_name_plural = 'Portfolio Items'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    @property
    def tech_list(self):
        """Return technologies as a list"""
        return [tech.strip() for tech in self.technologies_used.split(',') if tech.strip()]


class BlogPost(models.Model):
    """Blog posts for SEO and thought leadership"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    excerpt = models.CharField(max_length=300, help_text="Brief summary for listings")
    content = models.TextField(help_text="Full blog post content (HTML allowed)")
    author_name = models.CharField(max_length=100, default="Gregory Woodruff")
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    is_published = models.BooleanField(default=False)
    published_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-published_date', '-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class ContactSubmission(models.Model):
    """Contact form submissions"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    company = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, help_text="Internal notes")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Submission'
        verbose_name_plural = 'Contact Submissions'
    
    def __str__(self):
        return f"{self.name} - {self.subject} ({self.created_at.strftime('%Y-%m-%d')})"
