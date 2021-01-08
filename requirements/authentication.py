# from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from user.models import User
from django.conf import settings
import jwt
# from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from functools import wraps

# class MyAuthentication(BaseAuthentication):
def create_token(id, email):
    try:
        token   =   jwt.encode({'user_id':id, 'user_email':email}, settings.SECRET_KEY, algorithm='HS256')
        return token
    except Exception:
        return JsonResponse({'error' : 'error creating token'})


def authenticate(function):
    def wrapper_function(*args, **kwargs):    
        try:
            request =   args[0].request
            encoded_token   =   request.headers['Token']
            decoded_token   =   jwt.decode(encoded_token, settings.SECRET_KEY, algorithms='HS256')
            # return JsonResponse({'id':decoded_token['user_id'], 'email':decoded_token['user_email']})
            # print(decoded_token['user_email'])
            return function(*args, **kwargs)
        except Exception as e:
            # print(str(e.__dict__))
            raise exceptions.AuthenticationFailed('invalid token')
    return wrapper_function