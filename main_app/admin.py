from django.contrib import admin

# Register your models here.

from .models import Kid, Feeding

admin.site.register([Kid, Feeding])