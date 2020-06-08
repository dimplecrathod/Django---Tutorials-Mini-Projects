from django.contrib import admin

from .models import City
from .models import Country

admin.site.register(City)
admin.site.register(Country)