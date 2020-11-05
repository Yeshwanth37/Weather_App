from django.contrib import admin
from .models import City

# admin.site.register(City)
  
@admin.register(City)
class City(admin.ModelAdmin):
    list_display = ['name']
