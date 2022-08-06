"""
WSGI config for BH_DJANGO project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BH_DJANGO.settings')

application = get_wsgi_application()

project_folder = os.path.expanduser('/home/kcaldonjr0587/resume_site/Resume')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))