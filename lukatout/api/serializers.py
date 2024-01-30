from rest_framework import serializers
from .models import Address, Province, City, Township, Country

class ProvinceSerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())
    class Meta:
        model = Province
        fields = ('id', 'label', 'country', 'created_by_user')
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        country = instance.country
        country_representation = CountrySerializer(country).data
        representation['country'] = {
            'id' : country_representation["id"],
            'label' : country_representation['label']
        }
        return representation

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'label', 'created_by_user', 'province' )

class TownshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Township
        fields = ('id', 'label', 'city', 'created_by_user')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'label', 'created_by_user')

class AddressSerializer(serializers.ModelSerializer):
    province = serializers.PrimaryKeyRelatedField(queryset=Province.objects.all())
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    township = serializers.PrimaryKeyRelatedField(queryset=Township.objects.all())

    class Meta:
        model = Address
        fields = ('id', 'province', 'city', 'township', 'created_by_user')
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        city = instance.city
        province = instance.province
        township = instance.township
        city_representation = CitySerializer(city).data
        province_representation = ProvinceSerializer(province).data
        township_representation = TownshipSerializer(township).data
        representation['city'] = {
            'id' : city_representation["id"],
            'label' : city_representation['label']
        }
        representation['province'] ={
            'id' : province_representation["id"],
            'label' : province_representation['label']
        }
        representation['country'] = province_representation['country']
    
        representation['township'] ={
            'id' : township_representation["id"],
            'label' : township_representation['label']
        }
        return representation
