# Generated by Django 3.2.4 on 2021-07-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credenciais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('tipo_credencial', models.CharField(choices=[('usuario_senha', 'Usuario e Senha'), ('chave_privada', 'Chave privada')], max_length=50)),
                ('usuario', models.CharField(blank=True, max_length=100, null=True)),
                ('senha', models.CharField(blank=True, max_length=100, null=True)),
                ('chave_privada', models.TextField(blank=True, null=True)),
            ],
        ),
    ]