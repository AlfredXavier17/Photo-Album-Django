from django.contrib import admin

# Register your models here.
from . models import Photos,Category
admin.site.register(Category)
admin.site.register(Photos)