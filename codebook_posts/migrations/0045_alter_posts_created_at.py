# Generated by Django 4.0.4 on 2022-06-17 05:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codebook_posts', '0044_alter_posts_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 17, 5, 18, 48, 165269, tzinfo=utc)),
        ),
    ]