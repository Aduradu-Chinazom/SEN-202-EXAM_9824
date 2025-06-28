from django.shortcuts import render

from rest_framework import viewsets
from .models import StaffBase, Manager, Intern
from .serializers import StaffBaseSerializer, ManagerSerializer, InternSerializer

class StaffBaseViewSet(viewsets.ModelViewSet):
    queryset = StaffBase.objects.all()
    serializer_class = StaffBaseSerializer

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class InternViewSet(viewsets.ModelViewSet):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer
