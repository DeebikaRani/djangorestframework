from django.template.backends import django
from django.contrib import admin
from .models import employee

admin.site.register(employee)