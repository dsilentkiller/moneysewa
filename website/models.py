from django.db import models
from django.utils import timezone
from django.shortcuts import render, redirect


class About(models.Model):
    img = models.ImageField()

    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Service(models.Model):
    img = models.ImageField()

    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    fullname = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.BigIntegerField()
    message = models.TextField()

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = "Contact Us"


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class SubscribedUsers(models.Model):
    email = models.EmailField(max_length=120, unique=True)
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField('Date Created', default=timezone.now)

    def __str__(self):
        return self.email


class Info (models.Model):
    location = models.CharField(max_length=400)
    office_phone = models.CharField(max_length=300)
    office_email = models.EmailField()
    social_media = models.CharField(max_length=100)

    def __str__(self):
        return self.location
