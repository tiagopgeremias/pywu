from django.contrib import admin
from django.forms import ModelForm, PasswordInput, CharField
from .models import Credenciais

class CredenciaisForm(ModelForm):
    senha = CharField(widget=PasswordInput(),max_length=100,required=False)
    class Meta:
        model = Credenciais
        fields = '__all__'
        

@admin.register(Credenciais)
class CredenciaisAdmin(admin.ModelAdmin):
    list_display = ['titulo','tipo_credencial']
    form = CredenciaisForm
    class Media:
        js = ('js/credenciais.js',)


