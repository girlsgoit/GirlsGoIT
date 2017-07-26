from django.db import models
from datetime import datetime
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
class Region(models.Model):
    name = models.CharField(max_length=30)
    thumbnail_img = models.CharField(max_length=200)
    hero_img = models.CharField(max_length=200)
    motto = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name

# Member model
class Member(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    photo = models.CharField(max_length=200)
    personal_page = models.CharField(max_length=200)
    region = models.ForeignKey(Region)

    def __str__(self):
        return self.name +' '+ self.surname

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
