from django.shortcuts import render
from .serializer import PlantSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Plants
from requirements import api_response
from rest_framework.serializers import ValidationError
from requirements import authentication

class PlantsView(APIView):
    @authentication.authenticate
    def get(self, request, id=None):
        try:
            if id is None:
                queryset    =   Plants.objects.all()
                serializer  =   PlantSerializer(queryset,  many=True)
                if queryset.count() == 0:
                    response    =   api_response.APIResponse(200,"", "No plants").respond()
            else:
                queryset    =   Plants.objects.get(pk=id)
                serializer  =   PlantSerializer(queryset)
            response    =   api_response.APIResponse(200, serializer.data).respond()
            return Response(response, status=status.HTTP_200_OK)

        except Plants.DoesNotExist as not_found_error:
            response    =   api_response.APIResponse(404, str(not_found_error), "plant not found").respond()
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            response    =   api_response.APIResponse(400, str(e)).respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @authentication.authenticate
    def post(self, request):
        try:
            data    =   request.data
            serializer  =   PlantSerializer(data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            response    =   api_response.APIResponse(200, "", "plant added").respond()
            return Response(response, status=status.HTTP_200_OK)

        except ValidationError as err:
            response    =   api_response.APIResponse(400, str(err), "Validation error").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            response    =   api_response.APIResponse(400, str(e)).respond()
            return Response(response)

    @authentication.authenticate
    def put(self, request, id):
        try:
            plant_instance  =   Plants.objects.get(pk=id)
            serializer      =   PlantSerializer(instance=plant_instance, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                plant   =   serializer.save()
                response    =   api_response.APIResponse(200, plant.plantId, "Plant Updated").respond()
                return Response(response, status=status.HTTP_200_OK)

        except ValidationError as err:
            response    =   api_response.APIResponse(400, str(err), "validation error").respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        except Plants.DoesNotExist as not_found_error:
            response = api_response.APIResponse(404, str(not_found_error), "plant with given id does not exist").respond()
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            response    =   api_response.APIResponse(400, str(e)).respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @authentication.authenticate
    def delete(self, request, id):
        try:
            plant_instance  =   Plants.objects.get(pk=id)
            plant_instance.delete()
            response    =   api_response.APIResponse(200, "", "Plant deleted").respond()
            return Response(response, status=status.HTTP_200_OK)
        
        except Plants.DoesNotExist as not_found_error:
            response = api_response.APIResponse(404, str(not_found_error), "plant with given id does not exist").respond()
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            response    =   api_response.APIResponse(400, str(e)).respond()
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
