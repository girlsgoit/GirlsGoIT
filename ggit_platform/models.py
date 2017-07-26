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


class Event(model.Model):
	title = models.CharField(max_length=50)
	short_description = models.TextField()
	start_date = models.DateTimeField()
	end_date = models.DateTimeField(null =True, blank=True)
	thumbnail_image = models.CharField(max_length=200)
	hero_image = models.CharField(max_length=200)
	aplly_form = models.CharField(max_length=200)
	long_description = MarkdownxField()
	application_start_date = models.DateTimeField(null=True, blank=True)
	application_end_date = models.DateTimeField(null=True, blank=True)
	region = models.ForeignKey("Region", null=True, blank=True)
# Story model

