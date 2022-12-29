from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.http.response import Http404
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.







class TouristAPIView(APIView):

    def get_object(self, pk):
        try:
            return Tourist.objects.filter(pk=pk)
        except Tourist.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
        else:
            data = Tourist.objects.all().order_by('id')
        serializer=TouristSerializer(data,many=True)
          
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        serializer = TouristSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'message': 'Tourist added successfully',
            'data': serializer.data
        }

        return Response(response,status=status.HTTP_200_OK)

    def put(self, request, pk=None, format=None):
        tourist_to_update = Tourist.objects.get(
            pk=pk)
        serializer = TouristSerializer(
            instance=tourist_to_update, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'message': 'Tourist Updated Successfully',
            'data': serializer.data
        }

        return Response(response,status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        tourist_to_update = Tourist.objects.get(
            pk=pk)

        tourist_to_update.delete()

        response = {
            'message': 'Tourist deleted Successfully',
        }

        return Response(response,status=status.HTTP_200_OK)
