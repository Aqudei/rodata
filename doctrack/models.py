from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from core.models import TimestampedModelMixin
from django.conf import settings

class Label(models.Model):

    name = models.CharField(_("Name"), max_length=50)
    description = models.TextField(null=True,blank=True)
    
    class Meta:
        verbose_name = _("label")
        verbose_name_plural = _("labels")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("label_detail", kwargs={"pk": self.pk})
# Create your models here.
class Document(TimestampedModelMixin):

    subject = models.CharField(max_length=400)    
    file = models.FileField(upload_to='documents/')
    parent = models.ForeignKey(
        "self", verbose_name=_("Parent"), on_delete=models.SET_NULL,null=True, blank=True)
    labels = models.ManyToManyField("doctrack.Label", through="doctrack.DocumentLabelRel", related_name='documents')
    
    class Meta:
        verbose_name = _("document")
        verbose_name_plural = _("documents")

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("document_detail", kwargs={"pk": self.pk})
    
class DocumentLabelRel(TimestampedModelMixin):

    document = models.ForeignKey("doctrack.Document", on_delete=models.CASCADE)
    label  = models.ForeignKey("doctrack.Label", on_delete=models.CASCADE)
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_("Actor"), on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = _("documentlabel rel")
        verbose_name_plural = _("documentlabel rels")

    def __str__(self):
        return f"{self.document} ({self.label})"

    def get_absolute_url(self):
        return reverse("documentlabelrel_detail", kwargs={"pk": self.pk})

