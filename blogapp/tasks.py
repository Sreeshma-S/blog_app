# tasks.py

from celery import shared_task
from django.utils import timezone
from blogapp.models import Post

@shared_task
def publish_scheduled_posts():
    scheduled_posts = Post.objects.filter(publish_date__lte=timezone.now(), published=False)
    for post in scheduled_posts:
        post.publish()
