from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Address, Province, City, Township
from .serializers import AddressSerializer, ProvinceSerializer, VilleSerializer, CommuneSerializer
from rest_framework.decorators import api_view

class AddressView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        List all the address for given requested user
        '''
        address = Address.objects.all()
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create all addresses and his dependencies
        '''
        data = {
            'Description': request.data.get('Description'), 
            'NomCategorie': request.data.get('NomCategorie'), 
        }
        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VilleView(APIView):
    def get (self, request, *args, **kwargs):
        '''get all ville'''
        cities = City.objects.all()
        serializer = VilleSerializer(cities, many=True)
        return Response({"code": 200, "args" : request.GET, "data" : serializer.data}, status=status.HTTP_200_OK)
    
class ProvinceView(APIView):
    def get (self, request, *args, **kwargs):
        '''get all ville'''
        cities = Province.objects.all()
        serializer = ProvinceSerializer(cities, many=True)
        return Response({"code": 200, "data" : serializer.data}, status=status.HTTP_200_OK)