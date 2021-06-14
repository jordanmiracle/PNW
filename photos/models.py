from django.db import models
from PNWproject.storage_backends import MediaStorage, PublicMediaStorage


class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False, storage=MediaStorage)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description
