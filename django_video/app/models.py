from django.db import models


class String(models.Model):
    title = models.CharField(max_length=200)
