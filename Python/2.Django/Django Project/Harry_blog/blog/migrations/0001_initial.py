# Generated by Django 3.0.8 on 2020-08-13 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('timestamp', models.DateField(blank=True)),
                ('img', models.ImageField(upload_to='blog/images')),
                ('slug', models.CharField(max_length=200)),
            ],
        ),
    ]
