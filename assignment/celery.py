import os

from celery import Celery
from finvid.constants import CELERY_FETCH_VIDEO_TIME_LIMIT

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignment.settings')

app = Celery('assignment')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'fetch-videos-every-30-seconds': {
        'task': 'finvid.tasks.fetch_videos',
        'schedule': CELERY_FETCH_VIDEO_TIME_LIMIT,
    },
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
