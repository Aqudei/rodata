from django.shortcuts import render
from rest_framework.viewsets import (ModelViewSet,)
from doctrack.models import (Document,Label, DocumentLabelRel)
from doctrack.serializers import DocumentSerializer
# Create your views here.


class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class =DocumentSerializer
    

