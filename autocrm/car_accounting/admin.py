from django.contrib import admin

from .models import Cars, Marks, Models
# Register your models here.

admin.site.register(Cars)
admin.site.register(Marks)
admin.site.register(Models)