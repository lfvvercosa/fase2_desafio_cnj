from django.db import models


class Vara(models.Model):
    name = models.TextField(max_length=500, blank=False)
    latitude = models.FloatField()
    longitude = models.FloatField()


