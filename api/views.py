from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from menu.models import Online_menu
from .serislizers import FoodsSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset= Online_menu.objects.all()
    serializer_class = FoodsSerializer
    permission_classes = IsAdminUser
