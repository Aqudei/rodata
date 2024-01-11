from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from core.models import TimestampedModelMixin
from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Requirement(TimestampedModelMixin):
    KINDS = (
        (0,'EEI'),
        (1,'RC'),
        (10,'OTHERS')
    )
    
    subject = models.CharField(max_length=255)
    attachments = GenericRelation("core.Attachment")
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True,blank=True)
    due = models.DateTimeField(auto_now=False, auto_now_add=False, null=True,blank=True)
    kind = models.PositiveIntegerField(choices=KINDS)
    origin = models.ForeignKey(
        "accounts.Department", on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        verbose_name = _("requirement")
        verbose_name_plural = _("requirements")

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("requirement_detail", kwargs={"pk": self.pk})

class Compliance(TimestampedModelMixin):
    subject = models.CharField(max_length=255)
    attachments = GenericRelation("core.Attachment")
    requirement = models.ForeignKey("requirements.Requirement", on_delete=models.CASCADE)
    point_person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = _("compliance")
        verbose_name_plural = _("compliances")

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("compliance_detail", kwargs={"pk": self.pk})
