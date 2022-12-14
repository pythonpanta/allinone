# Generated by Django 4.0 on 2022-07-02 08:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clg_api', '0015_alter_product_date_created_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 2, 14, 19, 39, 54209), null=True),
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('district_id', models.ForeignKey(db_column='district_id', on_delete=django.db.models.deletion.PROTECT, related_name='+', to='clg_api.district')),
                ('province_id', models.ForeignKey(db_column='province_id', on_delete=django.db.models.deletion.PROTECT, related_name='+', to='clg_api.province')),
            ],
            options={
                'db_table': 'municipality',
            },
        ),
    ]
