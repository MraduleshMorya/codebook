# Generated by Django 4.0.4 on 2022-05-10 12:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codebook_posts', '0026_alter_posts_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 10, 12, 38, 53, 167973, tzinfo=utc)),
        ),
    ]
