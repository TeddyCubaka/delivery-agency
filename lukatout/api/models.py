from django.db import models
from django.contrib.auth.models import User

class Province(models.Model):
    '''province modal'''
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=50)
    created_by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        '''db table's name'''
        db_table = 'rf_province'

class Ville(models.Model):
    '''province modal'''
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=50)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    created_by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        '''db table's name'''
        db_table = 'rf_ville'

class Commune(models.Model):
    '''province modal'''
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=50)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    created_by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        '''db table's name'''
        db_table = 'rf_commune'

class Address(models.Model):
    '''
        class modal for all address in the system.
    '''
    id = models.AutoField(primary_key=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    created_by_user = models.ForeignKey(User, on_delete=models.CASCADE)  
    class Meta:
        '''class meta for this modal'''
        db_table = 'op_address'