# Generated by Django 3.2.4 on 2021-06-24 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0006_grupoestacoes_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalGrupoEstacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_estacoes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='grupoestacoes',
            name='total',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventario.totalgrupoestacoes'),
            preserve_default=False,
        ),
    ]
