from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class TimestampedModelMixin(models.Model):

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)
                

    class Meta:
        abstract = True


class Attachment(TimestampedModelMixin):
    
    file = models.FileField(upload_to='attachments/', max_length=100)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    
    class Meta:
        verbose_name = _("attachment")
        verbose_name_plural = _("attachments")

    def __str__(self):
        return self.file.name

    def get_absolute_url(self):
        return reverse("attachment_detail", kwargs={"pk": self.pk})
