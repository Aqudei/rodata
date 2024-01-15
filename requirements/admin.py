from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from core.models import Attachment
from .models import (Requirement,Compliance)
import nested_admin


# Register your models here.
class AttachmentInline(nested_admin.NestedGenericTabularInline):
    model = Attachment
    extra = 1
    
class ComplianceInline(nested_admin.NestedStackedInline):
    model = Compliance
    extra = 1
    inlines = (AttachmentInline,)
    
@admin.register(Requirement)
class RequirementAdmin(nested_admin.NestedModelAdmin):
    list_display = ('control_num','subject','parent','due','kind','created_at','modified_at')
    search_fields = ('subject',)
    list_filter = ('kind',)
    inlines = (AttachmentInline, ComplianceInline)


@admin.register(Compliance)
class ComplianceAdmin(nested_admin.NestedModelAdmin):
    list_filter = ('control_num','subject','requirement','submission_date','point_person')
    search_fields = ('subject','control_num')
    list_filter = ('point_person',)
    inlines = (AttachmentInline,)
    
    
