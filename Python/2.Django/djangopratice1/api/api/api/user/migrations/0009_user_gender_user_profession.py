# Generated by Django 4.0 on 2022-06-30 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_user_pan_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='profession',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]