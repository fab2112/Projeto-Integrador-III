# Registros/models.py
from django.contrib.auth import get_user_model, get_user
from django.db import models
from django.urls import reverse
import sys

TITLE_CHOICES = [
    ('Em Extinção', 'Em Extinção'),
    ('Abundante', 'Abundante'),
]


class Registro(models.Model):
    nome_popular = models.CharField(max_length=255, verbose_name='Nome popular')
    nome_cientifico = models.CharField(max_length=255, verbose_name='Nome científico')
    especie = models.CharField(max_length=255, verbose_name='Espécie')
    altura_max = models.CharField(max_length=255, verbose_name='Altura máxima')
    diametro = models.CharField(max_length=255, verbose_name='Diâmetro nominal (cm)')
    bairro = models.CharField(max_length=255, verbose_name='Bairro')
    local = models.CharField(max_length=255, verbose_name='Localização')
    clima = models.CharField(max_length=255, verbose_name='Clima')
    regiao = models.CharField(max_length=255, verbose_name='Região')
    origem = models.CharField(max_length=255, verbose_name='Origem')
    latitude = models.CharField(max_length=255, verbose_name='Latitude')
    longitude = models.CharField(max_length=255, verbose_name='Longitude')
    extincao = models.CharField(max_length=255, verbose_name='Ameaça de extinção', choices=TITLE_CHOICES)
    desc = models.TextField(blank=True, verbose_name='Texto descritivo')
    data_1 = models.DateTimeField(auto_now_add=True, verbose_name='Data')
    image = models.ImageField(verbose_name='Upload imagem')

    def save(self, *args, **kwargs):
        try:
            this = Registro.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        except:
            #raise sys.exc_info()[0]
            pass
        super(Registro, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super(Registro, self).delete(*args, **kwargs)
        storage.delete(path)

    def __str__(self):
        return self.nome_popular

    def get_absolute_url(self):
        return reverse('registro_list')


class Comentario(models.Model):
    registro = models.ForeignKey(Registro, on_delete=models.CASCADE, related_name='comentarios', )
    comentario = models.CharField(max_length=500, blank=False, verbose_name='Menssagem')
    data_2 = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data')
    autor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        return reverse('registro_list')
