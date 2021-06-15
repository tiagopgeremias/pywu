from django.db import models
from django.forms import ModelForm, PasswordInput


# Create your models here.
class SSH_Credential(models.Model):
  
  _choice_credential = [
    ('userpass','Username and Password'),
    ('pemkey', 'SSH Key .pem'),
  ]
  
  description = models.CharField(max_length=100,blank=False,null=False)
  type = models.CharField(choices=_choice_credential, max_length=50)
  username = models.CharField(max_length=100,blank=False,null=False)
  password = models.CharField(max_length=50)
  sshkey = models.TextField(verbose_name="SSH Key", blank=True, null=True)

  def __str__(self):
    return f'{self.description}: {self.type}'
  
  class Meta:
    verbose_name_plural = "SSH Credentials"
    verbose_name = "SSH Credential"


class SSH_CredentialForm(ModelForm):
  ...