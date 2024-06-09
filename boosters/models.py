from django.contrib.auth.models import User
from django.db import models


class BoosterProfile(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='booster_photos/')
    rank = models.CharField(max_length=50)
    orders_completed = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0.0)
    boosting_for = models.CharField(max_length=100)
    languages = models.CharField(max_length=100)

    def __str__(self):
        return self.name
