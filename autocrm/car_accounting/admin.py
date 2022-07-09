from django.contrib import admin

from .models import Car, Mark, Model
# Register your models here.

admin.site.register(Car)
admin.site.register(Mark)
admin.site.register(Model)
