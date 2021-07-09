# Generated by Django 3.2.4 on 2021-06-24 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20210624_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupoestacoes',
            name='filtros',
        ),
        migrations.AddField(
            model_name='filtroestacoes',
            name='grupo_estacoes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventario.grupoestacoes'),
            preserve_default=False,
        ),
    ]