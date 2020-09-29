from django.shortcuts import render
from employee.models import Employee, Accessory
from employee.serializers import EmployeeSerializer, AccessorySerializer
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]


class AccessoryViewSet(viewsets.ModelViewSet):
    queryset = Accessory.objects.all().order_by('id')
    serializer_class = AccessorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]


