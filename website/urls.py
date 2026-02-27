from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    # Homepage
    path('', views.home, name='home'),
    
    # Services
    path('services/', views.services, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    
    # Portfolio
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/<slug:slug>/', views.portfolio_detail, name='portfolio_detail'),
    
    # Special showcases
    path('education/', views.education, name='education'),
    path('healthcare/', views.healthcare, name='healthcare'),
    
    # Blog
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_post, name='blog_post'),
    
    # Contact
    path('contact/', views.contact, name='contact'),
    
    # Generic pages (catch-all - must be last)
    path('<slug:slug>/', views.page_detail, name='page_detail'),
]
