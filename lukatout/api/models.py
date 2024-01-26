from django.db import models
from user.models import User
from django.utils import timezone

class Country(models.Model):
    '''rf_country modal'''
    id = models.UUIDField(primary_key=True)
    label = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_user = models.ForeignKey(User, models.PROTECT)
    class Meta:
        '''db table's name'''
        db_table = 'rf_country'

class Province(models.Model):
    '''province modal'''
    id = models.UUIDField(primary_key=True)
    label = models.CharField(max_length=50)
    country = models.ForeignKey(Country, models.PROTECT, default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_user = models.ForeignKey(User, models.PROTECT)
    class Meta:
        '''db table's name'''
        db_table = 'rf_province'

class City(models.Model):
    '''province modal'''
    id = models.UUIDField(primary_key=True)
    label = models.CharField(max_length=50)
    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_user = models.ForeignKey(User, on_delete=models.PROTECT)
    class Meta:
        '''db table's name'''
        db_table = 'rf_city'

class Township(models.Model):
    '''province modal'''
    id = models.UUIDField(primary_key=True)
    label = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_user = models.ForeignKey(User, on_delete=models.PROTECT)
    class Meta:
        '''db table's name'''
        db_table = 'rf_township'

class Address(models.Model):
    ''' class modal for all address in the system. '''
    id = models.UUIDField(primary_key=True)
    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    city = models.ForeignKey(City, on_delete=models.PROTECT, default=None)
    township = models.ForeignKey(Township, on_delete=models.PROTECT, default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_user = models.ForeignKey(User, models.PROTECT, related_name='addresses')  
    class Meta:
        '''class meta for this modal'''
        db_table = 'op_address'
