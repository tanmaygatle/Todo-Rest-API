from django.contrib import admin
from .models import Note,Todo

# Register your models here.
admin.site.register(Note)
admin.site.register(Todo)