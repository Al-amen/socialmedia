# Generated by Django 5.1.3 on 2024-12-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id_use',
            field=models.IntegerField(default=1),
        ),
    ]