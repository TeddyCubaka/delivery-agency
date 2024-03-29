from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from .models import User, Person, Agent
from .serializers import UserSerializer, PersonSerializer, AgentSerializer, TokenObtainSerializer
from api.views import Address, AddressSerializer
from .utils import Utils

class Auth :
    def generate_token(user):
        access_token = AccessToken.for_user(user)
        refresh_token = RefreshToken.for_user(user)
        access_token_string = str(access_token)
        refresh_token_string = str(refresh_token)

        return {'access' : access_token_string, 'refresh' : refresh_token_string}

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

class LoginView(APIView):
    def post(self, request):
        login = request.data.get('login')
        password = request.data.get('password')
        response = {
            'code' : 400,
            'message': 'la connexion a échoué.',
            'data': []
        }

        if login == None or password == None:
            response['code'] = 400
            response['message'] = 'Certaines clés sont manquantes'
            response['error'] = {
                'code' : 'missed_key',
                'message' : 'Verify that if the key password or login are in your body'
            }
            return Response(response, status=400)
        try:
            if Utils.is_number(login):
                user = User.objects.get(phone_number=login)
            elif Utils.is_valid_email(login):
                user = User.objects.get(email=login)
            else :
                response['code'] = 400
                response['message'] = 'Certaines clés sont manquantes'
                response['error'] = {
                    'code' : 'missed_key',
                    'message' : 'Verify that if the key password or login are in your body',
                    'data' : { 'key' : 'the login format is not allows' }
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

            if check_password(password, user.password):
                user_serializer = UserSerializer(user, many=False, context={'request': request})
                if user_serializer.data['is_active'] == 0 :
                    response['message'] = 'la connexion a échoué'
                    response['error'] = {
                        'code' : 'unactivate_account',
                        'message' : 'this account is not activated'
                    }
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)
                user_id = user_serializer.data['id']
                agent = Agent.objects.get(created_by_user_id=user_id)

                agent_serializer = AgentSerializer(agent, many=False, context={'request': request})
                agent_id = agent_serializer.data['id']
                del agent_serializer.data['id']
                response['code'] = 200
                response['message'] = 'la connexion a échoué'
                response['data'] = {
                    'user_id': user_id,
                    'agent_id': agent_id,
                    **agent_serializer.data,
                    'token' : Auth.generate_token(user)
                }
                return Response( response, status=status.HTTP_200_OK)
            else:
                response['message'] = 'mot de passe, numéro de téléphone ou email incorrect'
                response['error'] = {
                    'code' : 'invalid_identifiant',
                    'message' : 'Verify if the login or the password are correct',
                    'data' : request.data['login']
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            response['message'] = 'mot de passe, numéro de téléphone ou email incorrect'
            response['error'] = {
                'code' : 'invalid_identifiant',
                'message' : 'Verify if the login or the password are correct',
                'data' : request.data['login']
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
