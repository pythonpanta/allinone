# Generated by Django 4.0 on 2022-07-07 21:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clg_api', '0032_alter_product_manufactured_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manufactured_date',
            field=models.DateField(default=datetime.datetime(2022, 7, 8, 3, 21, 42, 694995), null=True),
        ),
    ]
