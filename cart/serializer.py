from rest_framework import serializers
from .models import Cart
from rest_framework.validators import UniqueTogetherValidator

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Cart
        fields  =   ('__all__')
        validators = [
            UniqueTogetherValidator(
                queryset=Cart.objects.all(),
                fields=['plant', 'customer']
            )
        ]

