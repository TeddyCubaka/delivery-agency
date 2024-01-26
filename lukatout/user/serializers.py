from rest_framework import serializers
from .models import User, Person, Agent, MerchantType, Merchant, ClientType, Client

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','phone_number','last_update','created_at','statut','is_connect','failed_login_count','two_factor_enabled','is_valid','is_active',
        ]

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','first_name','middle_name','last_name','sex','phone','email','photo_url','address_id','created_by_user']

class AgentSerialiser(serializers.ModelSerializer):
    person = PersonSerializer()
    class Meta:
        model = Agent
        fiels = '__all__'
