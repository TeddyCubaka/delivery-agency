from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Address, Province, City, Township, Country
from .serializers import AddressSerializer, ProvinceSerializer, CitySerializer, TownshipSerializer, CountrySerializer
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError

class AddressView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        '''List all the address for given requested user'''
        data = {
            'province': request.data.get('province'),
            'city': request.data.get('city'), 
            'township': request.data.get('township'), 
            'created_by_user': request.data.get('created_by_user'),
        }
        # address = Address.objects.filter(**data)
        address = Address.objects.all()
        serializer = AddressSerializer(address, many=True, context={'request': request})
        response_message = f"nous avons {len(serializer.data)} adresse{'s' if len(serializer.data) > 1 else ''} enreigistrée{'s' if len(serializer.data) > 1 else ''}"
        return Response({"code": 200, 'message' : response_message, "data" : serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''Create all addresses and his dependencies'''
        try:
            data = {
                'province': request.data.get('province'),
                'city': request.data.get('city'), 
                'township': request.data.get('township'), 
                'created_by_user': request.data.get('created_by_user'),
            }
            serializer = AddressSerializer(data=data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                response_data = {
                    'code': 201,
                    'message': 'adresse créé',
                    'data': serializer.data
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
            response_data = {
                'code': 400,
                'message': 'adresse non créée',
                'data': serializer.errors
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as err:
            response_data = {
                'code': 500,
                'message': 'une erreur s\'est produite',
                'data': err.detail
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

class CityView(APIView):
    def get (self, request, *args, **kwargs):
        '''get all city'''
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        response_message = f"nous avons {len(serializer.data)} ville{'s' if len(serializer.data) > 1 else ''} enreigistré"
        return Response({"code": 200, 'message' : response_message, "data" : serializer.data}, status=status.HTTP_200_OK)
    def post (self, request, *args, **kwargs):
        ''' city registration '''
        data = {
            'label': request.data.get('label'), 
            'province': request.data.get('province'), 
            'created_by_user': request.data.get('created_by_user'), 
        }
        serializer = CitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'code' : 201,
                'message' : 'ville enreigistrée',
                'data' : serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        response_data = {
            'code' : 400,
            'message' : 'ville non enreigistré',
            'data' : serializer.errors
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        
    
class ProvinceView(APIView):
    def get (self, request, *args, **kwargs):
        '''get all province'''
        cities = Province.objects.all()
        serializer = ProvinceSerializer(cities, many=True)
        response_message = f"nous avons {len(serializer.data)} province {'s' if len(serializer.data) > 1 else ''} enreigistré"
        return Response({"code": 200, 'message' : response_message, "data" : serializer.data}, status=status.HTTP_200_OK)
    def post (self, request, *args, **kwargs):
        ''' province registration '''
        data = {
            'label': request.data.get('label'), 
            'country': request.data.get('country'), 
            'created_by_user': request.data.get('created_by_user'), 
        }
        serializer = ProvinceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'code' : 201,
                'message' : 'province enreigistrée',
                'data' : serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        response_data = {
            'code' : 400,
            'message' : 'province non enreigistré',
            'data' : serializer.errors
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
    
class CountryView(APIView):
    def get (self, request, *args, **kwargs):
        '''get all country'''
        cities = Country.objects.all()
        serializer = ProvinceSerializer(cities, many=True)
        response_message = f"nous avons {len(serializer.data)} pays enreigistré"
        return Response({"code": 200, 'message' : response_message, "data" : serializer.data}, status=status.HTTP_200_OK)

    def post (self, request, *args, **kwargs):
        ''' country registration '''
        data = {
            'label': request.data.get('label'), 
            'acronym': request.data.get('acronym'), 
            'created_by_user': request.data.get('created_by_user'), 
        }
        serializer = CountrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'code' : 201,
                'message' : 'pays enreigistré',
                'data' : serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        response_data = {
            'code' : 400,
            'message' : 'pays non enreigistré',
            'data' : serializer.errors
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

class TownshipView(APIView):
    def get (self, request, *args, **kwargs):
        '''get all city'''
        cities = Township.objects.all()
        serializer = TownshipSerializer(cities, many=True)
        response_message = f"nous avons {len(serializer.data)} commune{'s' if len(serializer.data) > 1 else ''} enreigistré"
        return Response({"code": 200, 'message' : response_message, "data" : serializer.data}, status=status.HTTP_200_OK)
    def post (self, request, *args, **kwargs):
        ''' city registration '''
        data = {
            'label': request.data.get('label'), 
            'city': request.data.get('city'), 
            'created_by_user': request.data.get('created_by_user'), 
        }
        serializer = TownshipSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'code' : 201,
                'message' : 'commune enreigistrée',
                'data' : serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        response_data = {
            'code' : 400,
            'message' : 'commune non enreigistré',
            'data' : serializer.errors
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)