from django.db import models


class Pet(models.Model):

    PET_CHOICES = (
        ('Buqa', 'Buqa'),
        ('Sigir', 'Sigir'),
        ('Buzoq', 'Buzoq'),
    )

    name = models.CharField(max_length=128)
    category = models.CharField(max_length=30, choices=PET_CHOICES)
    age = models.FloatField()
    weight = models.FloatField()
    sold_will = models.DateField(blank=False)
    sold_was = models.DateField(null=True, blank=False)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Milk(models.Model):
    cow_id = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='milk')
    liters = models.FloatField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.date} kun /{self.liters} liter sut"


class Fodder(models.Model):
    title = models.CharField(max_length=128)
    cost = models.FloatField()
    size = models.FloatField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
