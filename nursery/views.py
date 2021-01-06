from django.shortcuts import render
from .models import Nursery
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from .serializer import NurserySerializer
from django.contrib.auth.hashers import make_password, check_password
from requirements import authentication,api_response
from rest_framework import status
from rest_framework.views import APIView

class LoginView(APIView):
    def post(self, request):
        try:
            email   =   request.data['email']
            password    =   request.data['password']
            nursery        =   Nursery.objects.get(email=email)
            # print(check_password(password, nursery.password))
            if nursery:
                if check_password(password, nursery.password):
                    token       =   authentication.MyAuthentication().create_token(nursery.nurseryId, nursery.email)
                    response    =   api_response.APIResponse(200, token).respond()
                    return Response(data=response, status=status.HTTP_200_OK)
                else:
                    response    =   api_response.APIResponse(401, "", "password is incorrect").respond()
                    return Response(response)
        except Exception as e:
            response    =   api_response.APIResponse(400, str(e), "nursery does not exist").respond()
            return Response(response)


class SignUpView(APIView):
    def post(self, request):
        try:
            serializer  =   NurserySerializer(data=request.data)
            if serializer.is_valid(raise_exception= True):
                serializer.save(password=make_password(request.data['password']))
                response    =   api_response.APIResponse(201, serializer.data, "Nursery registered successfully").respond()
                return Response(response, status=status.HTTP_201_CREATED)
                
        except Exception as e:
            response    =   api_response.APIResponse(400, str(e), "Data error").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)