# Generated by Django 4.0 on 2022-07-05 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clg_api', '0017_category_alter_product_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 5, 14, 38, 23, 449783), null=True),
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
    ]
