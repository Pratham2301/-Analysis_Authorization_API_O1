from logging import logMultiprocessing
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import InfoSerializer, LoginInfoKeySerializer
from django.contrib import messages

###############################################################################


@api_view(['POST'])
def Register(request):

    if request.method == 'POST':
        serializer = InfoSerializer(data=request.data)

        if serializer.is_valid():
            print(serializer.validated_data['name'])
            print(serializer.validated_data['email'])
            print(serializer.validated_data['college'])

            email1 = serializer.validated_data['email']

            data = Info.objects.filter(email=email1)

            if(len(data) == 0):
                serializer.save()
                print("saved")
                messages.success(request, 'REGISTERED SUCCESSFULLY')
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print("not saved")
                messages.error(request, 'EMAIL ALREADY EXIST',extra_tags='email')
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

###############################################################################


@api_view(['POST'])
def Login(request):

    if request.method == 'POST':
        serializer = LoginInfoKeySerializer(data=request.data)
        
        # print("got data")

        if serializer.is_valid():
            
            # print("got validity")
            
            email1 = serializer.validated_data['email']
            college1 = serializer.validated_data['college']
            key1 = serializer.validated_data['key']

            print(email1)
            print(college1)
            print(key1)

            data = Info.objects.filter(email=email1)

            if(len(data) == 1):
                print("Registered")
                
                if(data[0].college == college1):
                    row = CollegeKey.objects.filter(college=college1)
                    obj=row[0]
                    
                    print("CORRECT COLLEGE")

                    print(obj.college)
                    print(obj.key)

                    if (obj.key == key1):
                        messages.success(request, 'LOGGED IN SUCCESSFULLY')
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        messages.error(request, 'WRONG KEY', extra_tags='key')
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    messages.error(request, 'WRONG COLLEGE NAME', extra_tags='key')
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                print("not registered")
                messages.error(request, 'YOU HAVE NOT REGISTERED', extra_tags='email')
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

###############################################################################
