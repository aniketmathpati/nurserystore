from .models import User
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework import status
from .serializer import UserSerializer
from django.contrib.auth.hashers import make_password, check_password
from requirements import authentication, api_response
# from rest_framework import permissions


class LoginView(APIView):
    # permission_classes = [permissions.AllowAny]
    def post(self, request):
        try:
            email   =   request.data['email']
            password    =   request.data['password']
            user        =   User.objects.get(email=email)
            # print(user.userId)
            # print(check_password(password, user.password))
            if user:
                if check_password(password, user.password):
                    token       =   authentication.MyAuthentication().create_token(user.userId, email)
                    response    =   api_response.APIResponse(200, token).respond()
                    return Response(data=response, status=status.HTTP_200_OK)
                else:
                    response    =   api_response.APIResponse(401, "", "password is incorrect").respond()
                    return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            response    =   api_response.APIResponse(400, str(e), "User does not exist").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class SignUpView(APIView):
    def post(self, request):
        try:
            serializer  =   UserSerializer(data=request.data)
            if serializer.is_valid(raise_exception= True):
                id          =   serializer.save(password=make_password(request.data['password']))
                response    =   api_response.APIResponse(201, "", "User registered successfully").respond()
                return Response(response)
                # return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            response    =   api_response.APIResponse(400, str(e), "Data error").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)