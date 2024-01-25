from django.db import models
from django.contrib.auth.models import User
# , AbstractUser

# class User(AbstractUser):
#     phone = models.CharField(max_length=9, unique=True)
#     def get_full_name(self):
#         '''get full name of a user'''
#         return f"{self.first_name} {self.last_name}"

#     def get_phone_number(self):
#         '''get user phone number'''
#         return self.phone

class Country(models.Model):
    '''rf_country modal'''
    id = models.UUIDField(primary_key=True)
    label = models.CharField(max_length=50)
    created_by_user = models.ForeignKey(User, models.PROTECT)
    class Meta:
        '''db table's name'''
        db_table = 'rf_country'

class Province(models.Model):
    '''province modal'''
    id = models.UUIDField(primary_key=True)
    label = models.CharField(max_length=50)
    country = models.ForeignKey(Country, models.PROTECT, default=1)
    created_by_user = models.ForeignKey(User, models.PROTECT)
    class Meta:
        '''db table's name'''
        db_table = 'rf_province'

class City(models.Model):
    '''province modal'''
    id = models.UUIDField(primary_key=True)
    label = models.CharField(max_length=50)
    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    created_by_user = models.ForeignKey(User, on_delete=models.PROTECT)
    class Meta:
        '''db table's name'''
        db_table = 'rf_city'

class Township(models.Model):
    '''province modal'''
    id = models.UUIDField(primary_key=True)
    label = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    created_by_user = models.ForeignKey(User, on_delete=models.PROTECT)
    class Meta:
        '''db table's name'''
        db_table = 'rf_township'

class Address(models.Model):
    '''
        class modal for all address in the system.
    '''
    id = models.UUIDField(primary_key=True)
    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    city = models.ForeignKey(City, on_delete=models.PROTECT, default=None)
    township = models.ForeignKey(Township, on_delete=models.PROTECT, default=1)
    created_by_user = models.ForeignKey(User, models.PROTECT)  
    class Meta:
        '''class meta for this modal'''
        db_table = 'op_address'

class Person(models.Model):
    '''
        rf_person model
    '''
    id = models.UUIDField(primary_key=True)
    first_name = models.TextField(max_length=30)
    middle_name = models.TextField(max_length=30)
    last_name = models.TextField(max_length=30)
    sex = models.CharField(max_length=1)
    phone = models.CharField(max_length=9)
    email = models.EmailField()
    photo_url = models.URLField()
    address_id = models.ForeignKey(Address, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_user = models.ForeignKey(User, models.PROTECT)

    class Meta:
        '''class meta for this modal'''
        db_table = 'rf_person'

class Agent(models.Model):
    '''
        op_agent model
    '''
    id = models.UUIDField(primary_key=True)
    as_person = models.ForeignKey(Person, on_delete=models.PROTECT)
    birth_place = models.TextField(max_length=30)
    # function_id = models.ForeignKey('rf_function', on_delete=models.PROTECT)
    # grade_id = models.ForeignKey('rf_grade', on_delete=models.PROTECT)
    born_at = models.DateField()
    hired_at = models.DateField()
    is_available = models.TextField(max_length=34)
    avenue = models.TextField(max_length=20)
    number = models.TextField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_user = models.ForeignKey(User, models.PROTECT)
    class Meta:
        '''class meta for this modal'''
        db_table = 'op_agent'

class MarchantType(models.Model):
    '''type | categorie of marchant'''
    id = models.UUIDField(primary_key=True)
    label = models.CharField(max_length=15)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_user = models.ForeignKey(User, models.PROTECT)

    class Meta:
        '''class meta for this modal'''
        db_table = 'rf_marchant_type'

class Marchant(models.Model):
    '''op_marchant model'''
    id = models.UUIDField(primary_key=True)
    reference_person = models.ForeignKey(Person, on_delete=models.PROTECT)
    code_postal = models.CharField(max_length=5)
    site_web = models.URLField()
    born_at = models.DateField()
    is_active = models.BooleanField()
    zip_code = models.CharField(max_length=5)
    society_name = models.CharField(max_length=50)
    marchant_type = models.ForeignKey(MarchantType, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_user = models.ForeignKey(User, models.PROTECT)

    class Meta:
        '''class meta for this modal'''
        db_table = 'op_marchant'

class ClientType(models.Model):
    '''rf_client_type model'''
    id = models.UUIDField(primary_key=True)
    label = models.CharField(max_length=15)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_user = models.ForeignKey(User, models.PROTECT)

    class Meta:
        '''class meta for this modal'''
        db_table = 'rf_client_type'

class Client (models.Model):
    '''op_client model'''
    id = models.UUIDField(primary_key=True)
    as_person = models.ForeignKey(Person, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=False)
    class Meta:
        '''class meta for this model'''
        db_table = 'op_client'