# Generated by Django 3.2.4 on 2021-06-25 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0012_auto_20210625_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupoestacoes',
            name='total_estacoes',
        ),
    ]
