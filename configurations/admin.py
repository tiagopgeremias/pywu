from django.contrib import admin
from .models import SSH_Credential, SSH_CredentialForm

# Register your models here.
@admin.register(SSH_Credential)
class SSH_CredentialAdmin(admin.ModelAdmin):
  form = SSH_CredentialForm
  search_fields = ('description',)
  list_display_links = ('id','description')
  list_display = ('id','description','username','type')

  
  