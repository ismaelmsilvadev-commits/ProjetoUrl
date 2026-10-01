import secrets
from django.db import models
from django.conf import settings


def gerar_codigo_unico():
  # Retorna uma string segura contendo letras e números (ex: 'aB3x9Z')
  # 4 bytes geram uma string de aproximadamente 6 caracteres, ideal para encurtadores
  return secrets.token_urlsafe(4)[:10]

# Create your models here.
class Link(models.Model):
    code = models.CharField(unique=True, max_length=10, default=gerar_codigo_unico)
    url_destination = models.URLField(max_length=2048)
    url_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url_destination

    class Meta:

        # Nome personalizado
        db_table = 'tb_link'

       

        verbose_name = 'Link'
        verbose_name_plural = 'Links'
