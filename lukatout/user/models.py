from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError("L'email est requis.")
        if not phone_number:
            raise ValueError("Le numéro de téléphone est requis.")

        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            **extra_fields
        )
        User.set_password(make_password(password))
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, phone_number, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12, unique=True)
    last_update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(default=timezone.now)
    statut = models.CharField(max_length=50, blank=True)
    is_connect = models.BooleanField(default=False) 
    failed_login_count = models.IntegerField(default=0) 
    two_factor_enabled = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = UserManager()

    def get_username(self):
        if self.email:
            return self.email
        return self.phone_number

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
    address_id = models.OneToOneField('api.Address', on_delete=models.PROTECT)
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

class MerchantType(models.Model):
    '''type | categorie of merchant'''
    id = models.UUIDField(primary_key=True)
    label = models.CharField(max_length=15)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_user = models.ForeignKey(User, models.PROTECT)

    class Meta:
        '''class meta for this modal'''
        db_table = 'rf_merchant_type'

class Merchant(models.Model):
    '''op_merchant model'''
    id = models.UUIDField(primary_key=True)
    reference_person = models.ForeignKey(Person, on_delete=models.PROTECT)
    code_postal = models.CharField(max_length=5)
    site_web = models.URLField()
    born_at = models.DateField()
    is_active = models.BooleanField()
    zip_code = models.CharField(max_length=5)
    society_name = models.CharField(max_length=50)
    merchant_type = models.ForeignKey(MerchantType, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_user = models.ForeignKey(User, models.PROTECT)

    class Meta:
        '''class meta for this modal'''
        db_table = 'op_merchant'

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