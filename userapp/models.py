from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Usuario(AbstractUser):
    class Meta:
    
            # Nome personalizado
            db_table = 'tb_usuarios'
    
           
    
            verbose_name = 'Usuario'
            verbose_name_plural = 'Usuarios'
