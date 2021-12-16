import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_heroku.settings')

app = Celery('test_heroku')

# app.conf.update(timezone = 'Asia/Bishkek')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery Beat Settings


app.autodiscover_tasks()


app.conf.beat_schedule = {
    "check_celery": {
        "task": "celery_test.tasks.test_funk",
        "schedule": crontab()
    },
}


# django channels websockets
@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')