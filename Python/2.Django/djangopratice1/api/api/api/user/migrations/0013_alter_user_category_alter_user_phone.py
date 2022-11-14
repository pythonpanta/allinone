# Generated by Django 4.0 on 2022-07-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clg_api', '0031_alter_product_manufactured_date'),
        ('user', '0012_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='category',
            field=models.ManyToManyField(blank=True, db_column='category_id', related_name='+', to='clg_api.Category'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
