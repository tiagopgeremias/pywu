# Generated by Django 3.2.4 on 2021-06-25 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0010_remove_filtroestacoes_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacoes',
            name='tipo_estacao',
            field=models.CharField(choices=[('servidor', 'servidor'), ('pdv', 'pdv'), ('farmaceutica', 'farmaceutica')], max_length=50),
        ),
    ]
