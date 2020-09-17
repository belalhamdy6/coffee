from rest_framework import serializers
from .models import *



class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class CoffeMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeMachine
        fields = '__all__'

class CoffeFlaverSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeFlaver
        fields = '__all__'


class PackSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackSize
        fields = '__all__'


class CoffePodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffePods
        fields = '__all__'