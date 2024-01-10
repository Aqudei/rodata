from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from core.models import TimestampedModelMixin
from django.conf import settings

class Department(TimestampedModelMixin):

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("department")
        verbose_name_plural = _("departments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("department_detail", kwargs={"pk": self.pk})


# Create your models here.
class UserProfile(TimestampedModelMixin):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,blank=True)
    employee_number = models.CharField(max_length=50)
    department = models.ForeignKey(
        "accounts.Department", on_delete=models.SET_NULL, null=True,blank=True) 
    
    class Meta:
        verbose_name = _("user profile")
        verbose_name_plural = _("user profiles")

    def __str__(self):
        return self.employee_number

    def get_absolute_url(self):
        return reverse("userprofile_detail", kwargs={"pk": self.pk})
