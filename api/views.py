from django.shortcuts import render
from rest_framework import viewsets
from api.models import company
from api.serializer import companySeralizer
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset= company.objects.all()
    serializer_class=companySeralizer
