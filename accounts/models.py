from django.db import models
from django.contrib.auth.models import User


class Accounts(User):
    definition = models.TextField(max_length=4096, null=True, blank=True)
    salary = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    passport = models.FileField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    phone_farm = models.CharField(max_length=13, null=True, blank=True)
    telegram = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.username
