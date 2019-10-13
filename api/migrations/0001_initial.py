# Generated by Django 2.2.6 on 2019-10-13 16:16

import api.models
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeoRef',
            fields=[
                ('code', models.CharField(editable=False, max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Referencia Geografica',
                'verbose_name_plural': 'Referencias Geograficas',
                'db_table': 'geo_ref',
            },
        ),
        migrations.CreateModel(
            name='Zones',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('1', 'ACTIVO'), ('0', 'INACTIVO'), ('2', 'NO DISPONIBLE')], default='2', max_length=2)),
                ('geo_type', models.CharField(choices=[('1', 'COLONIA'), ('2', 'BARRIO'), ('3', 'PASAJE'), ('4', 'CANTON'), ('5', 'CASERI0')], default='1', max_length=2)),
                ('coordinates', djongo.models.fields.ArrayModelField(blank=True, model_container=api.models.CoordinateZone)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.GeoRef')),
            ],
            options={
                'verbose_name': 'Zona',
                'db_table': 'zones',
            },
        ),
        migrations.CreateModel(
            name='DangerRangeZone',
            fields=[
                ('added', models.DateTimeField(auto_created=True)),
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('code_danger', models.IntegerField(choices=[(1, 'Todo para ir bien'), (2, 'Conduzcase con cuidado'), (3, 'Mantengase alerta'), (4, 'Si puede evite la zona'), (5, 'No ingrese a la zona')], default=1, verbose_name='Nivel')),
                ('is_presencia_de_delincuentes', models.BooleanField(verbose_name='Existe presencia de delincuentes en la zona')),
                ('is_ingresar_a_la_zona_controlado', models.BooleanField(verbose_name='Ingresar a la zona es controlado por pandillas')),
                ('is_existe_renta_por_entrar_habitar', models.BooleanField(verbose_name='Existe algun tipo de renta para entrar o habitar a la zona')),
                ('is_drogas', models.BooleanField(verbose_name='Se rumora de ventas de drogas en la zona')),
                ('hora_minima', models.TimeField(verbose_name='Desde')),
                ('hora_maxima', models.TimeField(verbose_name='Hasta')),
                ('asesinatos', models.BooleanField()),
                ('robo_asaltos', models.BooleanField()),
                ('agresion_acoso', models.BooleanField()),
                ('robo_autos', models.BooleanField()),
                ('acoso_sexual', models.BooleanField()),
                ('vandalismo', models.BooleanField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Zones', verbose_name='Elige la zona')),
            ],
            options={
                'verbose_name': 'Indice de peligro',
                'verbose_name_plural': 'Indices de peligro',
                'db_table': 'zones_danger_rates',
            },
        ),
        migrations.CreateModel(
            name='CommentsZone',
            fields=[
                ('date', models.DateTimeField(auto_created=True)),
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('txt', models.TextField()),
                ('user', models.CharField(max_length=100)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Zones')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
                'db_table': 'zones_comments',
            },
        ),
    ]
