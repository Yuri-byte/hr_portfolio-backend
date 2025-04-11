from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee, Role, ContactInfo, EmployeeRoleHistory
from .serializers import (
    EmployeeSerializer, RoleSerializer, ContactInfoSerializer, EmployeeRoleHistorySerializer
)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

class EmployeeRoleHistoryViewSet(viewsets.ModelViewSet):
    queryset = EmployeeRoleHistory.objects.all()
    serializer_class = EmployeeRoleHistorySerializer