from rest_framework import serializers
from menu.models import Online_menu

class FoodsSerializer(serializers.ModelSerializer):
    name = Online_menu
    fields= '__all__'