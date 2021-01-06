from django.shortcuts import render
from .serializer import OrderSerializer
from rest_framework.views import APIView
from .models import Order
from requirements import api_response
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ValidationError
from plants.models import Plants

class OrderByUserView(APIView):
    def get(self, request, userId):
        try:
            queryset  =   Order.objects.filter(customer=userId)
            if queryset.count() == 0:
                raise Order.DoesNotExist()
            serializer  =   OrderSerializer(queryset, many=True)
            response    =   api_response.APIResponse(200, serializer.data).respond()
            return Response(response, status=status.HTTP_200_OK)

        except Order.DoesNotExist as e:
            response    =   api_response.APIResponse(404, str(e), "No orders").respond()
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            response    =   api_response.APIResponse(400, str(e), "Data error").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            serializer  =   OrderSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            response    =   api_response.APIResponse(200, serializer.data, "Order placed").respond()
            return Response(response, status=status.HTTP_200_OK)
        
        except ValidationError as e:
            response    =   api_response.APIResponse(400, str(e), "validation error occured").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            response    =   api_response.APIResponse(400, str(e), "Data error").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, userId):
        try:
            # print(request.data)
            order_instances   =   Order.objects.filter(customer=userId)
            if order_instances.count() == 0:
                raise Order.DoesNotExist()
            for order_instance in order_instances:
                for temp in request.data:
                    # print(temp['plant'] == cart_instance.plant.plantId)
                    if temp['customer'] == order_instance.customer.userId:
                        print(temp)
                        serializer      =   OrderSerializer(instance=order_instance, data=temp, partial=True)
                        if serializer.is_valid(raise_exception=True):
                            serializer.save()
                            print(serializer.data)
            response    =   api_response.APIResponse(200, "", "Order details changed").respond()
            return Response(response, status=status.HTTP_200_OK)

        except ValidationError as e:
            response    =   api_response.APIResponse(400, str(e), "Validation error occured").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        except Order.DoesNotExist as e:
            response    =   api_response.APIResponse(404, "", "order details not found for given user").respond()
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            response    =   api_response.APIResponse(400, str(e), "Data error").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class OrderByNurseryView(APIView):
    def get(self, request, nurseryId):
        try:
            queryset    =   Order.objects.filter(seller=nurseryId)
            if queryset.count() == 0:
                raise Order.DoesNotExist()
            serializer  =   OrderSerializer(queryset, many=True)
            response    =   api_response.APIResponse(200, serializer.data).respond()
            return Response(response, status=status.HTTP_200_OK)

        except Order.DoesNotExist as e:
            response    =   api_response.APIResponse(404, str(e), "No orders").respond()
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            response    =   api_response.APIResponse(400, str(e), "Data error").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, nurseryId):
        try:
            # print(request.data)
            order_instances   =   Order.objects.filter(seller=nurseryId)
            if order_instances.count() == 0:
                raise Order.DoesNotExist()
            for order_instance in order_instances:
                for temp in request.data:
                    if temp['seller'] == order_instance.seller.nurseryId:
                        print(temp)
                        serializer      =   OrderSerializer(instance=order_instance, data=temp, partial=True)
                        if serializer.is_valid(raise_exception=True):
                            serializer.save()
                            print(serializer.data)
            response    =   api_response.APIResponse(200, "", "Order details changed").respond()
            return Response(response, status=status.HTTP_200_OK)

        except ValidationError as e:
            response    =   api_response.APIResponse(400, str(e), "Validation error occured").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        except Order.DoesNotExist as e:
            response    =   api_response.APIResponse(404, "", "order details not found for given seller").respond()
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            response    =   api_response.APIResponse(400, str(e), "Data error").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)