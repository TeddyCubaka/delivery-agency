from rest_framework import serializers
from .models import User, Person, Agent, MerchantType, Merchant, ClientType, Client
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','phone_number','last_update','created_at','statut','is_connect','failed_login_count','two_factor_enabled','is_valid','is_active','password'
        ]
    def create (self, validated_data):
        user = User(
            email = validated_data['email'],
            phone_number = validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','first_name','middle_name','last_name','sex','phone','email','photo_url','address_id','created_by_user']

class AgentSerialiser(serializers.ModelSerializer):
    person = PersonSerializer()
    class Meta:
        model = Agent
        fiels = '__all__'
