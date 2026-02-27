from django.contrib import admin
from .models import Page, Service, PortfolioItem, BlogPost, ContactSubmission


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_published', 'show_in_navigation', 'order', 'updated_at']
    list_filter = ['is_published', 'show_in_navigation']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_published', 'show_in_navigation', 'order']
    fieldsets = (
        ('Page Content', {
            'fields': ('title', 'slug', 'content')
        }),
        ('SEO Settings', {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Display Options', {
            'fields': ('is_published', 'show_in_navigation', 'order')
        }),
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_featured', 'is_active', 'order', 'pricing_info']
    list_filter = ['category', 'is_featured', 'is_active']
    search_fields = ['title', 'short_description', 'full_description']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_featured', 'is_active', 'order']
    fieldsets = (
        ('Service Information', {
            'fields': ('title', 'slug', 'category', 'short_description', 'full_description')
        }),
        ('Display Settings', {
            'fields': ('icon_class', 'pricing_info', 'is_featured', 'is_active', 'order')
        }),
    )


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_type', 'client_name', 'completion_date', 'is_featured', 'is_published']
    list_filter = ['project_type', 'is_featured', 'is_published', 'completion_date']
    search_fields = ['title', 'short_description', 'client_name', 'technologies_used']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_featured', 'is_published']
    date_hierarchy = 'completion_date'
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'slug', 'project_type', 'client_name', 'short_description', 'full_description')
        }),
        ('Technical Details', {
            'fields': ('technologies_used', 'project_url', 'case_study_url')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Publishing', {
            'fields': ('completion_date', 'is_featured', 'is_published', 'order')
        }),
    )


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author_name', 'published_date', 'is_published', 'created_at']
    list_filter = ['is_published', 'published_date', 'author_name']
    search_fields = ['title', 'excerpt', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_published']
    date_hierarchy = 'published_date'
    fieldsets = (
        ('Post Content', {
            'fields': ('title', 'slug', 'author_name', 'excerpt', 'content', 'featured_image')
        }),
        ('SEO Settings', {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Publishing', {
            'fields': ('is_published', 'published_date')
        }),
    )


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'company', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'company', 'subject', 'message']
    list_editable = ['is_read']
    readonly_fields = ['name', 'email', 'company', 'phone', 'subject', 'message', 'created_at']
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'company', 'phone')
        }),
        ('Message', {
            'fields': ('subject', 'message', 'created_at')
        }),
        ('Status', {
            'fields': ('is_read', 'notes')
        }),
    )
    
    def has_add_permission(self, request):
        # Contact submissions come from the public form only
        return False


# Customize admin site header and title
admin.site.site_header = "Cloud Certified Support Admin"
admin.site.site_title = "CCS Admin Portal"
admin.site.index_title = "Content Management"
