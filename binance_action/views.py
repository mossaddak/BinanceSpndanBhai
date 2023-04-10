# from django.shortcuts import render
import random

from binance_action.binance_connection import Connection
from binance_action.serializers import BinanceConnectSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
 


@api_view(['POST'])
@permission_classes([])
def binance_connection(request):
    data = request.data
    binance_api_key = data['api_key']
    binance_api_secret = data['api_secret']
    client = Connection(binance_api_key, binance_api_secret)
    if client is not None:
        connection = {'binance_api_key': binance_api_key, 'binance_api_secrect': binance_api_secret}
        serializer = BinanceConnectSerializer(connection, many=False)
        return Response({'connection': 'Successfully Connected', 'api': serializer.data}, status=status.HTTP_200_OK)
    
    return Response({'error': 'Connection Problem. Please Check Your API Key and Secrect'})
    
