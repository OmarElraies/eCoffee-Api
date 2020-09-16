
from rest_framework import serializers
from .models import CoffeeMachine, CoffeePod
#from rest_framework_mongoengine import serializers


class CoffeeMachineSerializer(serializers.Serializer):
    product_code = serializers.CharField()
    product_label = serializers.CharField()


class CoffeePodSerializer(serializers.Serializer):
    product_code = serializers.CharField()
    product_label = serializers.CharField()
