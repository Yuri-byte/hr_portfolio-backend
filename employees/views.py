from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee, Role, ContactInfo, EmployeeRoleHistory
from .serializers import (
    EmployeeSerializer, RoleSerializer, ContactInfoSerializer, EmployeeRoleHistorySerializer
)
from .utils import build_employee_tree

@api_view(['GET'])
def employee_tree_view(request):
    ceo = Employee.objects.filter(manager=None).first()
    if not ceo:
        return Response({"error": "No root employee found."}, status=404)

    data = build_employee_tree(ceo)
    return Response(data)

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