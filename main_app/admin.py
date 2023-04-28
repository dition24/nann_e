from django.contrib import admin

# Register your models here.

from .models import Kid, Event, Photo

admin.site.register([Kid, Event, Photo])