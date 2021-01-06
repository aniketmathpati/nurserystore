from rest_framework import serializers
from .models import Plants
from rest_framework.validators import UniqueTogetherValidator

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Plants
        fields  =   ('__all__')
        validators = [
            UniqueTogetherValidator(
                queryset=Plants.objects.all(),
                fields=['plantId', 'sellerId']
            )
        ]