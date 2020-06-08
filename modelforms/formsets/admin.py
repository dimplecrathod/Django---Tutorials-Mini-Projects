from django.contrib import admin
from .models import Example, Programmer, Language, UserProfile

admin.site.register(Example)
admin.site.register(Programmer)
admin.site.register(Language)
admin.site.register(UserProfile)


# Register your models here.
