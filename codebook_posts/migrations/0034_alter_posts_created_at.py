# Generated by Django 4.0.4 on 2022-05-24 11:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codebook_posts', '0033_alter_posts_created_at_notifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 24, 11, 27, 48, 719687, tzinfo=utc)),
        ),
    ]
