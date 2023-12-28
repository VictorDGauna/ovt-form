from django.contrib import admin
from import_export.admin import ExportActionModelAdmin
from .models import Bildens_model
from .resources import Bildens_modelResouce

class DisplayAdmin(ExportActionModelAdmin):
    resources_class = Bildens_modelResouce
    list_display = ['name', 'lastName','email']
    search_fields = ['name', 'lastName','email']

admin.site.register(Bildens_model, DisplayAdmin)