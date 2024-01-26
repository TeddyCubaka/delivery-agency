from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password

from .models import User
from .serializers import UserSerializer

class SignupView(APIView):
    def post(self, request):
        user_data = {
            "email" : request.data.get('email'),
            'phone_number' : request.data.get('phone_number'),
            'password' : request.data.get('password')
        }
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)