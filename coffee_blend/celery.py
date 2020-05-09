import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffee_blend.settings')

app = Celery('coffee_blend')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
