from django.urls import path
from .views import *

app_name = 'machine'
urlpatterns = [
    path('api/ProductTypeList', ProductTypeList.as_view(), name='ProductTypeList'),
    path('api/CoffeMachineList', CoffeMachineList.as_view(), name='CoffeMachineList'),
    path('api/CoffeFlaverList', CoffeFlaverList.as_view(), name='CoffeFlaverList'),
    path('api/PackSizeList', PackSizeList.as_view(), name='PackSizeList'),
    path('api/CoffePodsList', CoffePodsList.as_view(), name='CoffePodsList'),
]