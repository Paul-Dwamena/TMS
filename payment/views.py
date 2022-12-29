from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.http.response import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from tourist.serializer import *

# Create your views here.







class PaymentAPIView(APIView):

    def get_object(self, pk):
        try:
            return Payment.objects.filter(pk=pk)
        except Payment.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
        else:
            data = Payment.objects.all().order_by('id')
        serializer=PaymentSerializer(data,many=True)
          
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        serializer = PaymentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'message': 'Payment added successfully',
            'data': serializer.data
        }

        return Response(response,status=status.HTTP_200_OK)

    def put(self, request, pk=None, format=None):
        payment_to_update = Payment.objects.get(
            pk=pk)
        serializer = PaymentSerializer(
            instance=payment_to_update, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'message': 'Payment Updated Successfully',
            'data': serializer.data
        }

        return Response(response,status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        payment_to_update = Payment.objects.get(
            pk=pk)

        payment_to_update.delete()

        response = {
            'message': 'Payment deleted Successfully',
        }

        return Response(response,status=status.HTTP_200_OK)



# endpoint to get a report of tourist names and the total amount they paid
@csrf_exempt
@api_view(['GET'])
def get_tourist_report(request):
    payments=Payment.objects.all()
    ser=PaymentSerializer(payments,many=True)
    allpayment=[]
    for i in ser.data:
        tourist = Tourist.objects.get(id=i['tourist_id'])
        serializer = TouristSerializer(tourist).data
        obj={
            'amount_paid':i['amount_paid'],
            'firstname':serializer['firstname'],
            'lastname':serializer['lastname']
        }
        allpayment.append(obj)

    data={
        'paymets':allpayment
    }
       
       

    return Response(data,status=status.HTTP_200_OK)



#  endpoint to select only those who did not pay for any tourist site
@csrf_exempt
@api_view(['GET'])
def paying_tourist(request):
    tourist = Tourist.objects.all()
    payments = Payment.objects.all()

    tourist_list = []
    for t in tourist:
        tourist_list.append(t.id)

    payment_list = []
    for p in payments:
        payment_list.append(p.tourist_id.id)

    paying_tourist = list(set(tourist_list) & set(payment_list))
    paying_tourist = Tourist.objects.filter(id__in=paying_tourist)
    serializer = TouristSerializer(paying_tourist, many=True)
      

    return Response(serializer.data,status=status.HTTP_200_OK)

        

  
    

#  endpoint to select only those who did not pay for any tourist site
@csrf_exempt
@api_view(['GET'])
def unpaid_tourist(request):
    tourist = Tourist.objects.all()
    payments = Payment.objects.all()
   

    tourist_list = []
    for t in tourist:
        tourist_list.append(t.id)

    payment_list = []
    for p in payments:
        payment_list.append(p.tourist_id.id)

    non_paying_tourist = list(set(tourist_list) - set(payment_list))
    non_paying_tourist = Tourist.objects.filter(id__in=non_paying_tourist)
    serializer = TouristSerializer(non_paying_tourist, many=True)

    return Response(serializer.data,status=status.HTTP_200_OK)

    
