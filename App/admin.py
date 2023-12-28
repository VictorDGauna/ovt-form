from django.contrib import admin
from .models import Bildens_model

class DisplayAdmin(admin.ModelAdmin):
    list_display = ['name', 'lastName','email']
    search_fields = ['name', 'lastName','email']

admin.site.register(Bildens_model, DisplayAdmin)