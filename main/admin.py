from django.contrib import admin
from .models import Pet, Milk, Fodder

admin.site.register([Pet, Milk, Fodder])


