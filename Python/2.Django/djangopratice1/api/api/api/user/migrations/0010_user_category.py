# Generated by Django 4.0 on 2022-07-05 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clg_api', '0019_alter_product_date_created'),
        ('user', '0009_user_gender_user_profession'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='category',
            field=models.ForeignKey(db_column='category_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='clg_api.category'),
        ),
    ]
