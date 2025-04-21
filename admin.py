from django.contrib import admin
from .models import Complaint, Admission, Result

# Registering models in the admin panel

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'date_submitted')
    search_fields = ('name', 'email', 'message')

class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'gender', 'parent_name', 'parent_contact', 'email')
    search_fields = ('name', 'parent_name', 'email')

class ResultAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'subject_1', 'subject_2', 'subject_3', 'subject_4', 'subject_5', 'total_score')
    search_fields = ('student_id',)

# Registering models
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Admission, AdmissionAdmin)
admin.site.register(Result, ResultAdmin)