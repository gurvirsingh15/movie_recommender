from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE',"movie_recommender.settings")

app = Celery('movie_recommender', backend='amqp', broker='amqp://')
app.config_from_object('django.conf:settings',namespace="CELERY")
app.autodiscover_tasks()
