from django.shortcuts import render

from rest_framework import viewsets
from .models import StaffBase, Manager, Intern
from .serializers import StaffBaseSerializer
from rest_framework import response
from rest_framework import APIview

class StaffRoleView(APIview):
    def get(self, request):
        staff = list(Manager.objects.all()) + list(Intern.objects.all())
        serializer = StaffBaseSerializer(staff, many=True)
        return response(serializer.data)
        