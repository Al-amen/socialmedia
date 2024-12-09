# Generated by Django 5.1.3 on 2024-12-09 19:08

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_profile_id_user_alter_profile_profileimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post_images')),
                ('caption', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 12, 10, 1, 8, 36, 741088))),
                ('no_of_likes', models.IntegerField(default=0)),
            ],
        ),
    ]