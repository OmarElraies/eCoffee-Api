
from rest_framework import generics
from django_filters import rest_framework as filters

from .models import CoffeeMachine, CoffeePod
from .serializers import CoffeeMachineSerializer, CoffeePodSerializer


class MachinesView(generics.ListAPIView):
    queryset = CoffeeMachine.objects.all()
    serializer_class = CoffeeMachineSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('product_type', 'water_line_compatible')


class PodsView(generics.ListAPIView):
    queryset = CoffeePod.objects.all()
    serializer_class = CoffeePodSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('product_type', 'flavor_type', 'pack_size')