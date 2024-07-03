from rest_framework import serializers
from .models import CartItem, Cycle

class CartItemSerializerAdd(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'user', 'cycle']
        read_only_fields = ['user']

class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cycle
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    cycle = CycleSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'user', 'cycle', 'quantity']