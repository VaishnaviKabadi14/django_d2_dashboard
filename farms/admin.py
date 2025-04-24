from django.contrib import admin
from .models import Farm, Field, Crop

admin.site.register(Farm)
admin.site.register(Field)
admin.site.register(Crop)