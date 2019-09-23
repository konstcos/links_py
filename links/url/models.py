from django.db import models


class Link(models.Model):
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    description = models.TextField(default='', blank=True)
    notes = models.TextField(default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url
