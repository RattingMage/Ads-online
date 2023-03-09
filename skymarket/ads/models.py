from django.conf import settings
from django.db import models

from users.models import User


class Ad(models.Model):
    # TODO добавьте поля модели здесь
    title = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to="ads_image", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    text = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ad = models.ForeignKey(Ad, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
