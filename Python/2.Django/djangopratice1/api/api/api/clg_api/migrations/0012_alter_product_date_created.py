# Generated by Django 4.0 on 2022-06-30 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clg_api', '0011_alter_product_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 30, 20, 21, 37, 564882), null=True),
        ),
    ]