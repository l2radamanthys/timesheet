# Generated by Django 3.1 on 2020-08-18 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0002_cliente_proyecto_tarea_tareaproyecto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareaproyecto',
            name='horas',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]