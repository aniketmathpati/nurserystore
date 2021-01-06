from .models import Nursery
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class NurserySerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Nursery
        fields  =   ('__all__')
        read_only_fields    =   ['nurseryId']
        write_only_fields   =   ['password']
        extra_kwargs    =   {
            'nurseryName': {'validators': [UniqueValidator(queryset=model.objects.all())]},
            'email': {'validators': [UniqueValidator(queryset=model.objects.all())]},
            'phone': {'validators': [UniqueValidator(queryset=model.objects.all())]},
        }