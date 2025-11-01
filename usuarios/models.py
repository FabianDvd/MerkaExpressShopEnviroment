from django.db import models


class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'roles'

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    correo_electronico = models.CharField(unique=True, max_length=100)
    contrasena = models.CharField(max_length=255)
    numero_celular = models.CharField(max_length=20, blank=True, null=True)
    foto_perfil = models.CharField(max_length=255, blank=True, null=True)
    id_rol = models.ForeignKey(Roles, models.DO_NOTHING, db_column='id_rol')

    class Meta:
        managed = False
        db_table = 'usuarios'
