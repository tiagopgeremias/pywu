# Generated by Django 3.2.4 on 2021-06-30 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0014_alter_grupoestacoes_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='estacoes',
            name='tipo_pdv',
            field=models.CharField(choices=[(None, '---'), ('omni_caixa', 'omni_caixa'), ('omni_balcao', 'omni_balcao'), ('pharmax', 'pharmax')], default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estacoes',
            name='endereco_ip',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='estacoes',
            name='hostname',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='estacoes',
            name='tipo_estacao',
            field=models.CharField(choices=[('servidor', 'servidor'), ('pdv', 'pdv'), ('retaguarda', 'retaguarda'), ('farmaceutica', 'farmaceutica')], max_length=50),
        ),
    ]
