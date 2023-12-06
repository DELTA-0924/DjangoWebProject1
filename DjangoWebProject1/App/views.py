from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView;
from rest_framework import status
from rest_framework.decorators import api_view,action
from .serializers import ApartamentSerialer,ManagerSerializer
from django.shortcuts import get_object_or_404
from datetime import datetime
from .models import Apartaments,Managers
from rest_framework import viewsets
from rest_framework import generics

@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def apartaments_detail(request,pk=None):
    if request.method == 'GET':
        if pk is not None:
            apartament=Apartaments.objects.get(pk=pk)
            serializer = ManagerSerializer(apartament)
            return Response(serializer.data)
            pass
        else:
            apartament=Apartaments.objects.all()
            serializer = ApartamentSerialer(apartament,many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        apartament_id = request.data.get('id')
        apartament = get_object_or_404(Apartaments, id=apartament_id )
        serializer = ApartamentSerialer(apartament, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        apartament=Apartaments.objects.get(pk=pk)
        apartament.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        serializer = ApartamentSerialer(data=request.data)
        if serializer.is_valid():
            serializer.save(date=datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def manager_detail(request,pk=None):

    if request.method == 'GET':
        if pk is not None:
            manager = Managers.objects.get(pk=pk)
            serializer = ManagerSerializer(manager)
            return Response(serializer.data)
        else:
            managers = Managers.objects.all()
            serializer = ManagerSerializer(managers, many=True)
            return Response(serializer.data)

    elif request.method == 'PUT':
        manager_id = request.data.get('id')
        manager = get_object_or_404(Managers, id=manager_id )
        serializer = ManagerSerializer(manager, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        manager = get_object_or_404(Managers, pk=pk)
        manager.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(dataCreated=datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    