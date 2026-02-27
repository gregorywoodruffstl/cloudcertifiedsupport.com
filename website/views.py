from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Page, Service, PortfolioItem, BlogPost, ContactSubmission


def home(request):
    """Homepage with featured services and portfolio"""
    featured_services = Service.objects.filter(is_active=True, is_featured=True)[:3]
    featured_portfolio = PortfolioItem.objects.filter(is_published=True, is_featured=True)[:4]
    recent_posts = BlogPost.objects.filter(is_published=True)[:3]
    
    context = {
        'featured_services': featured_services,
        'featured_portfolio': featured_portfolio,
        'recent_posts': recent_posts,
    }
    return render(request, 'website/home.html', context)


def services(request):
    """Services page - all active services grouped by category"""
    all_services = Service.objects.filter(is_active=True)
    
    # Group services by category
    services_by_category = {}
    for service in all_services:
        category = service.get_category_display()
        if category not in services_by_category:
            services_by_category[category] = []
        services_by_category[category].append(service)
    
    context = {
        'services_by_category': services_by_category,
        'all_services': all_services,
    }
    return render(request, 'website/services.html', context)


def service_detail(request, slug):
    """Individual service detail page"""
    service = get_object_or_404(Service, slug=slug, is_active=True)
    related_services = Service.objects.filter(
        is_active=True,
        category=service.category
    ).exclude(id=service.id)[:3]
    
    context = {
        'service': service,
        'related_services': related_services,
    }
    return render(request, 'website/service_detail.html', context)


def portfolio(request):
    """Portfolio page with all projects"""
    project_type = request.GET.get('type', '')
    
    projects = PortfolioItem.objects.filter(is_published=True)
    if project_type:
        projects = projects.filter(project_type=project_type)
    
    # Pagination
    paginator = Paginator(projects, 9)  # 9 projects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get all project types for filter
    project_types = PortfolioItem.PROJECT_TYPE_CHOICES
    
    context = {
        'page_obj': page_obj,
        'project_types': project_types,
        'current_type': project_type,
    }
    return render(request, 'website/portfolio.html', context)


def portfolio_detail(request, slug):
    """Individual portfolio item detail page"""
    project = get_object_or_404(PortfolioItem, slug=slug, is_published=True)
    related_projects = PortfolioItem.objects.filter(
        is_published=True,
        project_type=project.project_type
    ).exclude(id=project.id)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'website/portfolio_detail.html', context)


def education(request):
    """Education hub - featuring YouBetYourAzure.com and learning resources"""
    context = {
        'youbetyourazure_url': 'https://youbetyourazure.com',
        'microsoft_learn_url': 'https://learn.microsoft.com',
    }
    return render(request, 'website/education.html', context)


def healthcare(request):
    """Healthcare solutions - featuring BrentwoodBlvd.com analytics platform"""
    # Get healthcare-related portfolio items
    healthcare_projects = PortfolioItem.objects.filter(
        is_published=True,
        project_type='HEALTHCARE'
    )
    
    context = {
        'brentwoodblvd_url': 'https://brentwoodblvd.com',
        'healthcare_projects': healthcare_projects,
    }
    return render(request, 'website/healthcare.html', context)


def blog(request):
    """Blog listing page"""
    posts = BlogPost.objects.filter(is_published=True)
    
    # Pagination
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'website/blog.html', context)


def blog_post(request, slug):
    """Individual blog post detail page"""
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    recent_posts = BlogPost.objects.filter(is_published=True).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'recent_posts': recent_posts,
    }
    return render(request, 'website/blog_post.html', context)


def contact(request):
    """Contact page with form submission"""
    if request.method == 'POST':
        # Create contact submission
        submission = ContactSubmission(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            company=request.POST.get('company', ''),
            phone=request.POST.get('phone', ''),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        submission.save()
        
        messages.success(request, 'Thank you for contacting us! We will respond within 24 hours.')
        return redirect('website:contact')
    
    return render(request, 'website/contact.html')


def page_detail(request, slug):
    """Generic page view for custom pages created in Django admin"""
    page = get_object_or_404(Page, slug=slug, is_published=True)
    
    context = {
        'page': page,
    }
    return render(request, 'website/page_detail.html', context)
