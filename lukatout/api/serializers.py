from rest_framework import serializers
from .models import Address
from .models import Province
from .models import Ville
from .models import Commune

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
        model = Ville
        fields = ('id', 'label', 'created_by_user', 'province' )

class CommuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commune
        fields = '__all__'