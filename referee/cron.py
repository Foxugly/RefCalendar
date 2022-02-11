from django.utils import timezone


def my_scheduled_job():
    print(timezone.now())
