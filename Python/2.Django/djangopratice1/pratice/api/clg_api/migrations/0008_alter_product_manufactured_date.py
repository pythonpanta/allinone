# Generated by Django 4.1.3 on 2022-11-03 03:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clg_api', '0007_alter_product_manufactured_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manufactured_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]