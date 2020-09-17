from django_filters.rest_framework import DjangoFilterBackend
from .serializer import *
from rest_framework import generics


class ProductTypeList(generics.ListAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_type_name_ar', 'product_type_name_en', 'product_type_enum']



class CoffeMachineList(generics.ListAPIView):
    queryset = CoffeMachine.objects.all()
    serializer_class = CoffeMachineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['water_line', 'coffe_machine_name_en', 'coffe_machine_name_ar']


class CoffeFlaverList(generics.ListAPIView):
    queryset = CoffeFlaver.objects.all()
    serializer_class = CoffeFlaverSerializer



class PackSizeList(generics.ListAPIView):
    queryset = PackSize.objects.all()
    serializer_class = PackSizeSerializer



class CoffePodsList(generics.ListAPIView):
    queryset = CoffePods.objects.all()
    serializer_class = CoffePodsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['coffe_pods_name_en', 'coffe_pods_name_ar']


