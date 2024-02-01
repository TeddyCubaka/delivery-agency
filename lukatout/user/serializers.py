from rest_framework import serializers
from .models import User, Person, Agent, MerchantType, Merchant, ClientType, Client
from django.contrib.auth.hashers import make_password
from api.serializers import AddressSerializer
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','phone_number','last_update','created_at','statut','is_connect','failed_login_count','two_factor_enabled','is_valid','is_active']

    def create (self, validated_data):
        user = User(
            email = validated_data['email'],
            phone_number = validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Le mot de passe doit contenir au moins 8 caractères.")
        return value

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','first_name','middle_name','last_name','sex','phone','email','photo_url','address','created_by_user']

class AgentSerializer(serializers.ModelSerializer):
    as_person = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all())
    created_by_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Agent
        fields = ['id','as_person', 'birth_place', 'born_at', 'hired_at', 'is_available', 'avenue', 'number', 'created_at', 'updated_at', 'created_by_user']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        as_person = instance.as_person
        created_by_user = instance.created_by_user

        as_person_representation = PersonSerializer(as_person).data
        created_by_user_representation = UserSerializer(created_by_user).data

        representation['as_person'] = as_person_representation
        representation['created_by_user'] = created_by_user_representation
    
        return representation

class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['id','email','phone_number','last_update','created_at','statut','is_connect','failed_login_count','two_factor_enabled','is_valid','is_active']
    def validate(self, validated_data):
        user = authenticate(phone_number=validated_data['username'], password=validated_data['password'])
        if not user:
            raise serializers.ValidationError('Identifiants invalides')
        return user


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

#     @classmethod
#     def get_token(cls, user):
#         token = super(MyTokenObtainPairSerializer, cls).get_token(user)

#         # Add custom claims
#         token['username'] = user.username
#         return token