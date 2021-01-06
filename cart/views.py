from django.shortcuts import render
from rest_framework.views import APIView
from .models import Cart
from .serializer import CartSerializer
from requirements import api_response
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ValidationError


class CartView(APIView):
    def get(self, request, userId):
        try:
            queryset    =   Cart.objects.filter(customer=userId)
            if queryset.count() == 0:
                raise Cart.DoesNotExist()
            serializer  =   CartSerializer(queryset, many=True)
            response    =   api_response.APIResponse(200, serializer.data).respond()
            return Response(response, status=status.HTTP_200_OK)
        except Cart.DoesNotExist as e:
            response    =   api_response.APIResponse(404, "", "cart details not found").respond()
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            response    =   api_response.APIResponse(400, str(e), "data error").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            serializer  =   CartSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            response    =   api_response.APIResponse(200, serializer.data, "Items added to cart").respond()
            return Response(response, status=status.HTTP_200_OK)
        
        except ValidationError as e:
            response    =   api_response.APIResponse(400, str(e), "Validation error occured").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            response    =   api_response.APIResponse(400, str(e), "Data error").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, userId):
        try:
            # print(request.data)
            cart_instances   =   Cart.objects.filter(customer=userId)
            if cart_instances.count() == 0:
                raise Cart.DoesNotExist()
            for cart_instance in cart_instances:
                for temp in request.data:
                    # print(temp['plant'] == cart_instance.plant.plantId)
                    if temp['plant'] == cart_instance.plant.plantId:
                        print(temp)
                        serializer      =   CartSerializer(instance=cart_instance, data=temp, partial=True)
                        if serializer.is_valid(raise_exception=True):
                            serializer.save()
                            print(serializer.data)
            response    =   api_response.APIResponse(200, "", "Cart updated").respond()
            return Response(response, status=status.HTTP_200_OK)

        except ValidationError as e:
            response    =   api_response.APIResponse(400, str(e), "Validation error occured").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        except Cart.DoesNotExist as e:
            response    =   api_response.APIResponse(404, "", "cart details not found for given user").respond()
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            response    =   api_response.APIResponse(400, str(e), "Data error").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, userId):
        try:
            cart_instances   =   Cart.objects.filter(customer=userId)
            for cart_instance in cart_instances:
                cart_instance.delete()
            response    =   api_response.APIResponse(200,"","Cart empty").respond
            return Response(response, status=status.HTTP_200_OK)
        
        except Cart.DoesNotExist as e:
            response    =   api_response.APIResponse(404, "", "cart details not found for given user").respond()
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            response    =   api_response.APIResponse(400, str(e), "Data error").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class CartUnitView(APIView):
    def delete(self, request, userId, plantId):
        try:
            cart_instances   =   Cart.objects.filter(customer=userId, plant=plantId)
            for cart_instance in cart_instances:
                cart_instance.delete()
            response    =   api_response.APIResponse(200,"","Item deleted").respond()
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            response    =   api_response.APIResponse(400, str(e), "Data error").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)