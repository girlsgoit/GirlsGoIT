from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField


# Track model
class Track(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.TextField()
    icon = models.CharField(max_length=100)
    hero_image = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = MarkdownxField()

    def __str__(self):
        return self.title


# Region model
class Region(models.Model):
    name = models.CharField(max_length=30)
    motto = models.TextField()
    thumbnail_image = models.CharField(max_length=200)
    hero_image = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


# Member models
class MemberRole(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    role = models.ForeignKey(MemberRole)
    photo = models.CharField(max_length=200)
    personal_page = models.CharField(max_length=200)
    region = models.ForeignKey(Region)

    def __str__(self):
        return self.name + ' ' + self.surname


# Event model
class Event(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    application_start_date = models.DateTimeField(null=True, blank=True)
    application_end_date = models.DateTimeField(null=True, blank=True)
    aplly_form = models.CharField(max_length=200)
    thumbnail_image = models.CharField(max_length=200)
    hero_image = models.CharField(max_length=200)
    region = models.ForeignKey(Region, null=True, blank=True)
    short_description = models.TextField()
    long_description = MarkdownxField()

    def __str__(self):
        return self.title


# Story model
class Story(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
    thumbnail_image = models.CharField(max_length=200)
    hero_image = models.CharField(max_length=200)
    region = models.ForeignKey(Region, blank=True, null=True)
    short_description = models.TextField()
    long_description = MarkdownxField()

    def __str__(self):
        return self.title
