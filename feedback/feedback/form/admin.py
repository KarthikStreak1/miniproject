from django.contrib import admin

from .models import Subject, Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('subject', 'student_name', 'date', 'happy',)
    list_filter = ('subject', 'date',)
    search_fields = ('subject__name', 'details',)

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Subject)


#---------------------------------------change ------------------------------------------
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin 
from .resource import ReportResource  
from .models import Report
class ReportAdmin(ImportExportModelAdmin):
     resource_class = ReportResource      
admin.site.register(Report, ReportAdmin)