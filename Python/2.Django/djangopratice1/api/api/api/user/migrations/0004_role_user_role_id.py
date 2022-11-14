# Generated by Django 4.0 on 2022-06-28 16:10

from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.CharField(default=user.models.uuid_generate, max_length=32, primary_key=True, serialize=False, unique=True)),
                ('role', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='role_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='user.role'),
        ),
    ]
