# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categorie(models.Model):
    categorieid = models.AutoField(db_column='CategorieId', primary_key=True)  # Field name made lowercase.
    nomcategorie = models.CharField(db_column='NomCategorie', max_length=15)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=2000, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categorie'


class Client(models.Model):
    clientid = models.CharField(db_column='ClientId', primary_key=True, max_length=5)  # Field name made lowercase.
    nomsociete = models.CharField(db_column='NomSociete', max_length=40)  # Field name made lowercase.
    contactnom = models.CharField(db_column='ContactNom', max_length=30, blank=True, null=True)  # Field name made lowercase.
    contacttitre = models.CharField(db_column='ContactTitre', max_length=30, blank=True, null=True)  # Field name made lowercase.
    adresse = models.CharField(db_column='Adresse', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ville = models.CharField(db_column='Ville', max_length=15)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=15, blank=True, null=True)  # Field name made lowercase.
    codepostal = models.CharField(db_column='CodePostal', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pays = models.CharField(db_column='Pays', max_length=15)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=24, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=24, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'client'


class Collation(models.Model):
    texte = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'collation'


class Division(models.Model):
    divisionid = models.PositiveIntegerField(db_column='DivisionId', primary_key=True)  # Field name made lowercase.
    nomdivision = models.CharField(db_column='NomDivision', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'division'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Fournisseur(models.Model):
    fournisseurid = models.AutoField(db_column='FournisseurId', primary_key=True)  # Field name made lowercase.
    nomsociete = models.CharField(db_column='NomSociete', max_length=40)  # Field name made lowercase.
    contactnom = models.CharField(db_column='ContactNom', max_length=30, blank=True, null=True)  # Field name made lowercase.
    contacttitre = models.CharField(db_column='ContactTitre', max_length=30, blank=True, null=True)  # Field name made lowercase.
    adresse = models.CharField(db_column='Adresse', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ville = models.CharField(db_column='Ville', max_length=15)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=15, blank=True, null=True)  # Field name made lowercase.
    codepostal = models.CharField(db_column='CodePostal', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pays = models.CharField(db_column='Pays', max_length=15)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=24, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=24, blank=True, null=True)  # Field name made lowercase.
    siteweb = models.CharField(db_column='SiteWeb', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fournisseur'


class Produit(models.Model):
    produitid = models.AutoField(db_column='ProduitId', primary_key=True)  # Field name made lowercase.
    nomproduit = models.CharField(db_column='NomProduit', max_length=40)  # Field name made lowercase.
    fournisseurid = models.ForeignKey(Fournisseur, models.DO_NOTHING, db_column='FournisseurId', blank=True, null=True)  # Field name made lowercase.
    categorieid = models.ForeignKey(Categorie, models.DO_NOTHING, db_column='CategorieId')  # Field name made lowercase.
    unitecontionnement = models.CharField(db_column='UniteContionnement', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prixunitaire = models.DecimalField(db_column='PrixUnitaire', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    quantiteenstock = models.SmallIntegerField(db_column='QuantiteEnStock', blank=True, null=True)  # Field name made lowercase.
    quantiteencommande = models.SmallIntegerField(db_column='QuantiteEnCommande', blank=True, null=True)  # Field name made lowercase.
    niveaureappro = models.SmallIntegerField(db_column='NiveauReappro', blank=True, null=True)  # Field name made lowercase.
    enrupture = models.PositiveIntegerField(db_column='EnRupture')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produit'


class Service(models.Model):
    divisionid = models.OneToOneField(Division, models.DO_NOTHING, db_column='DivisionId', primary_key=True)  # Field name made lowercase. The composite primary key (DivisionId, ServiceId) found, that is not supported. The first column is selected.
    serviceid = models.SmallIntegerField(db_column='ServiceId')  # Field name made lowercase.
    nomservice = models.CharField(db_column='NomService', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'service'
        unique_together = (('divisionid', 'serviceid'),)


class Sysdiagrams(models.Model):
    diagram_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, db_collation='utf8_general_ci')
    principal_id = models.IntegerField()
    version = models.IntegerField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Transporteur(models.Model):
    transporteurid = models.AutoField(db_column='TransporteurId', primary_key=True)  # Field name made lowercase.
    nomsociete = models.CharField(db_column='NomSociete', max_length=40)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=24, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transporteur'
