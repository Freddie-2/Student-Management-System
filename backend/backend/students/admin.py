from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student

models_list = [Student]
admin.site.register(models_list)