# Generated by Django 4.2.1 on 2023-06-20 20:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_inscripcion',
            field=models.DateField(verbose_name=datetime.date(2023, 6, 20)),
        ),
    ]
