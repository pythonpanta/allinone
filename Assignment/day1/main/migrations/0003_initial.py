# Generated by Django 4.1.3 on 2022-11-02 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_delete_stuent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stuent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=244)),
                ('roll', models.IntegerField()),
                ('address', models.CharField(max_length=244)),
            ],
        ),
    ]
