from django.db import models


class Favorite(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default="None")
