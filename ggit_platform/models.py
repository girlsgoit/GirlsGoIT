from django.db import models
from datetime import datetime

# Track model


# Region model


# Member model


# Event model


# Story model
class Story(models.Model):
    title = models.CharField(max_lenght=100)
    short_descr = models.TextField()
    create_date = models.DateTimeField(defaul=datetime.now())
    thumbnail_image = models.CharField(max_lenght=200)
    subtitle = models.CharField(max_lenght=200)
    long_desc = models.MarkdownFieldx()
    region = ForeignKey("Region", blank=True, null=True)
