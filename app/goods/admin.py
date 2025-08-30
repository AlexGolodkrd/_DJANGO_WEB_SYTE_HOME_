from django.contrib import admin

# Register your models here.
from goods.models import Categories, Products

admin.site.register(Products)
admin.site.register(Categories)