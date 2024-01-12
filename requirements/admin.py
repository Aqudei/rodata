from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from core.models import Attachment
from .models import (Requirement,Compliance)

class ComplianceInline(admin.StackedInline):
    model = Compliance

# Register your models here.
class AttachmentInline(GenericTabularInline):
    model = Attachment
    
@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('control_num','subject','parent','due','kind','created_at','modified_at')
    search_fields = ('subject',)
    list_filter = ('kind',)
    inlines = (AttachmentInline, ComplianceInline)


@admin.register(Compliance)
class ComplianceAdmin(admin.ModelAdmin):
    list_filter = ('control_num','subject','requirement','submission_date','point_person')
    search_fields = ('subject','control_num')
    list_filter = ('point_person',)
    inlines = (AttachmentInline,)
    
    
