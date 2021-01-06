# from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from user.models import User
from django.conf import settings
import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

class MyAuthentication(BaseAuthentication):
    def create_token(self, id, email):
        try:
            token   =   jwt.encode({'user_id':id, 'user_email':email}, settings.SECRET_KEY, algorithm='HS256')
            return token
        except Exception:
            return JsonResponse({'error' : 'error creating token'})

    
    def authenticate(self, request):
        # print(request.headers)
        try:
            encoded_token   =   request.headers['Token']
            decoded_token   =   jwt.decode(encoded_token, settings.SECRET_KEY, algorithms='HS256')
            return JsonResponse({'id':decoded_token['user_id'], 'email':decoded_token['user_email']})
        except Exception:
            raise exceptions.AuthenticationFailed('invalid token')