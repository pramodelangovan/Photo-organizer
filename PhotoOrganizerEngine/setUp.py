import os
import sys

import django

path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'PhotoOrganizerApi')
sys.path.append(path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PhotoOrganizerApi.settings')
django.setup()
