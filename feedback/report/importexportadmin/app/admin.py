from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin 
from .resource import ReportResource  
from .models import Report
class ReportAdmin(ImportExportModelAdmin):
     resource_class = ReportResource      
admin.site.register(Report, ReportAdmin)