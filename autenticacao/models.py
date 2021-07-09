from django.db import models

# Create your models here.
class Credenciais(models.Model):
    
    tipo_credencial_choice = [
        ('usuario_senha','Usuario e Senha'),
        ('chave_privada','Chave privada')
    ]
    
    titulo = models.CharField(max_length=100, blank=False, null=False)
    tipo_credencial = models.CharField(max_length=50,choices=tipo_credencial_choice)
    usuario = models.CharField(max_length=100, blank=True, null=True)
    senha = models.CharField(max_length=100, blank=True, null=True)
    chave_privada = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.titulo