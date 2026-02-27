#!/bin/bash
# Import services from SQLite export into Azure PostgreSQL database

echo "🔄 Importing services into Azure PostgreSQL database..."
echo ""

# Run Django loaddata command
python manage.py loaddata services_export.json

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ SUCCESS! Services imported successfully!"
    echo ""
    echo "Imported data:"
    python manage.py shell -c "
from website.models import Service, Page, PortfolioItem, BlogPost
print(f'  ✓ Services: {Service.objects.count()}')
print(f'  ✓ Pages: {Page.objects.count()}')
print(f'  ✓ Portfolio Items: {PortfolioItem.objects.count()}')
print(f'  ✓ Blog Posts: {BlogPost.objects.count()}')
"
    echo ""
    echo "🌐 Visit https://cloudcertifiedsupport.com/services to see your services!"
else
    echo ""
    echo "❌ Import failed. Check error messages above."
    exit 1
fi
