from django.db import models

# Track model


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

