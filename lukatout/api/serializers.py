from rest_framework import serializers
from .models import Address, Province, City, Township

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id','province_id','ville_id','commune_id','created_by_user_id']


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'

class VilleSerializer(serializers.ModelSerializer):
    province = ProvinceSerializer()
    class Meta:
        model = City
        fields = ('id', 'label', 'created_by_user', 'province' )

class CommuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Township
        fields = '__all__'