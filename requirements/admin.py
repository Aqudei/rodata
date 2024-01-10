from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from core.models import Attachment
from .models import (Requirement,Compliance)

# Register your models here.
class AttachmentInline(GenericTabularInline):
    model = Attachment
    
@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('subject','parent','due','kind','created_at','modified_at')
    search_fields = ('subject',)
    list_filter = ('kind',)
    inlines = (AttachmentInline,)


@admin.register(Compliance)
class ComplianceAdmin(admin.ModelAdmin):
    list_filter = ('subject','requirement','submission_date','point_person')
    search_fields = ('subject',)
    list_filter = ('point_person',)
    inlines = (AttachmentInline,)
    
    