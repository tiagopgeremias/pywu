# Generated by Django 3.2.4 on 2021-07-01 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0002_remove_credenciais_senha'),
    ]

    operations = [
        migrations.AddField(
            model_name='credenciais',
            name='senha',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
