from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Farm(models.Model):
    name = models.CharField(max_length=512, null=True, blank=True)
    admin = User
    address = models.CharField(max_length=512, null=True, blank=True)
    images = models.FileField(null=True, blank=True)


class StaffUser(models.Model):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    definition = models.TextField(max_length=4096, null=True, blank=True)
    salary = models.CharField(max_length=255, null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    passport = models.FileField(null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    phone_farm = models.CharField(max_length=13, null=True, blank=True)
    telegram = models.CharField(max_length=128, null=True, blank=True)

