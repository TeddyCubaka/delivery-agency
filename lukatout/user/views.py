from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password

from .models import User, Person, Agent
from .serializers import UserSerializer, PersonSerializer, AgentSerializer
from api.views import AddressView, Address, AddressSerializer

class SignupView(APIView):
    def post(self, request):
        user_type = request.data.get('user_type')
        user_data = {
            "email" : request.data.get('email'),
            'phone_number' : request.data.get('phone_number'),
            'password' : request.data.get('password')
        }
        address_data = {
            'province' : request.data.get('province'),
            'city' : request.data.get('city'),
            'township' : request.data.get('township')
        }
        person_data = {
            'first_name' : request.data.get("first_name"),
            'middle_name' : request.data.get("middle_name"),
            'last_name' : request.data.get("last_name"),
            'sex' : request.data.get("sex"),
            'phone' : request.data.get("phone_number"),
            'email' : request.data.get("email"),
            'photo_url' : request.data.get("photo_url"),
            'user_type' : user_type,
        }
        user_to_create = {}
        match user_type :
            case 'A' :
                user_to_create = {
                    'birth_place' : request.data.get('birth_place'),
                    'born_at' : request.data.get('born_at'),
                    'hired_at' : request.data.get('hired_at'),
                    'is_available' : request.data.get('is_available'),
                    'avenue' : request.data.get('avenue'),
                    'number' : request.data.get('number'),
                }
            case default :
                response ={
                    'code' : 400,
                    'message' : 'ce d\'utilisateur n\'est pas correct',
                    'error' : {
                        'code' : 0,
                        'key' : {'user_type': user_type},
                        'data' : request.data
                    }
                }
                return Response(response)
        address = Address.objects.filter(**address_data)
        user_serializer = AddressSerializer(address, many=True, context={'request': request})
        existed_addresses = user_serializer.data

        if len(existed_addresses) == 0:
            return Response({'code' : 200, 'message' : 'this address is not exist', 'data': []})
        else :
            person_data['address'] = existed_addresses[0].get('id')

        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            user_data = user_serializer.data
            del user_data['password']
        else : return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        person_data['created_by_user'] = user_data['id']
        user_to_create['created_by_user'] = user_data['id']

        person_serializer = PersonSerializer(data=person_data)
        if person_serializer.is_valid():
            person_serializer.save()
            user_to_create['as_person'] = person_serializer.data['id']
        else :
            User.objects.filter(id=user_data['id']).delete()
            return Response({'code' : 500, 'message' : 'Une erreur s\'est produite', 'error': {'code' : 0, 'data' : person_serializer.errors}}, status=status.HTTP_400_BAD_REQUEST) 

        user_to_create_serializer = None
        match user_type :
            case 'A' :
                user_to_create_serializer = AgentSerializer(data=user_to_create)

        if user_to_create_serializer is None : return Response({'code' : 500, 'message' : 'Une erreur s\'est produite', 'data': []})
        if user_to_create_serializer.is_valid():
            user_to_create_serializer.save()
            return Response({'code' : 201, 'message' : 'agent created', 'data': user_to_create_serializer.data})
        else : 
            Person.objects.filter(id=person_serializer.data['id']).delete()
            User.objects.filter(id=user_data['id']).delete()
            return Response(user_to_create_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 