#!/usr/bin/env python
"""Export services to clean UTF-8 JSON without BOM"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cloudcertifiedsupport.settings')
django.setup()

from django.core import serializers
from website.models import Service, Page, PortfolioItem, BlogPost

# Get all objects
services = Service.objects.all()
pages = Page.objects.all()
portfolio = PortfolioItem.objects.all()
blogs = BlogPost.objects.all()

# Combine all objects
all_objects = list(services) + list(pages) + list(portfolio) + list(blogs)

print(f"Found {len(all_objects)} objects to export:")
print(f"  - Services: {len(services)}")
print(f"  - Pages: {len(pages)}")
print(f"  - Portfolio Items: {len(portfolio)}")
print(f"  - Blog Posts: {len(blogs)}")

# Serialize to JSON with UTF-8 encoding (no BOM)
json_data = serializers.serialize('json', all_objects, indent=2)

# Write with explicit UTF-8 encoding without BOM
with open('services_clean.json', 'w', encoding='utf-8') as f:
    f.write(json_data)

print(f"\n✅ Exported to services_clean.json ({len(json_data)} bytes)")
print("Ready to upload to Azure!")
