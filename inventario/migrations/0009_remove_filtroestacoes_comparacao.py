# Generated by Django 3.2.4 on 2021-06-25 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0008_auto_20210624_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filtroestacoes',
            name='comparacao',
        ),
    ]
