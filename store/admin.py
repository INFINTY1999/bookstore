from django.contrib import admin

# Register your models here.

from .models import Profile,Store,Books

admin.site.register(Profile)
admin.site.register(Store)
admin.site.register(Books)