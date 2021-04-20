import datetime

from django.db import models


class Reviews(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    name = models.CharField(blank=True, null=True, max_length=50)
    title = models.TextField(blank=False, null=False, max_length=100)
    description = models.TextField(blank=False, null=False, max_length=1000)
    date = models.DateTimeField(datetime.datetime.now())
    rating = models.IntegerField(RATING_CHOICES)
