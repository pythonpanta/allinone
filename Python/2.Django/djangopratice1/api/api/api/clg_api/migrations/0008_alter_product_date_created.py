# Generated by Django 4.0 on 2022-06-28 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clg_api', '0007_alter_customer_creaed_at_alter_customer_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 28, 21, 55, 19, 628148), null=True),
        ),
    ]