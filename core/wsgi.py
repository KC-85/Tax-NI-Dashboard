import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'wsgi' application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tax_ni_dashboard.settings')

# Get the WSGI application instance
application = get_wsgi_application()
