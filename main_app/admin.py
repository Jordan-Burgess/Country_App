from django.contrib import admin
from .models import Country, Continent, Language

# Register your models here.

admin.site.register(Country)
admin.site.register(Continent)
admin.site.register(Language)