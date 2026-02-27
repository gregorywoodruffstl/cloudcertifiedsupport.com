import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cloudcertifiedsupport.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Create superuser if doesn't exist
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='gregory.woodruff@cloudcertifiedsupport.com',
        password='CloudCertified2026!'
    )
    print('✅ Superuser created successfully!')
    print('Username: admin')
    print('Password: CloudCertified2026!')
    print('')
    print('⚠️  IMPORTANT: Change this password after first login!')
else:
    print('Superuser already exists.')
