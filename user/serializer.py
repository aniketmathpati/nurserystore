from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   User
        fields  =   ('__all__')
        extra_kwargs = {
            'email': {'validators': [UniqueValidator(queryset=model.objects.all())]},
            'phone': {'validators': [UniqueValidator(queryset=model.objects.all())]},
        }