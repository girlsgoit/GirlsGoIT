from django.db import models
from markdownx.models import MarkdownxField

# Track model
class Track(models.Model):
    title = models.CharField(max_length=50)
    icon = models.CharField(max_length=100)
    short_description = models.TextField()
    subtitle = models.TextField()
    hero_imgae= models.CharField(max_length=200)
    long_description = MarkdownxField()


# Region model


# Member model


# Event model


# Story model

