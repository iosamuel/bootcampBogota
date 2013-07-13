from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UsuariosManager(BaseUserManager):
    def create_user(self, username, nombre, apellido, password=None):
        if not username:
            raise ValueError('El usuario debe tener un username')
        user = self.model(username=username, nombre=nombre, apellido=apellido)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, nombre, apellido, password):
        user = self.create_user(username, nombre, apellido, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Usuarios(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=250, unique=True, db_index=True)
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)

    objects = UsuariosManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombre', 'apellido']

class Entradas(models.Model):
	nombre = models.CharField(max_length=250)
	texto = models.TextField()
	usuario = models.ForeignKey(Usuarios)

	def __unicode__(self):
		return self.nombre