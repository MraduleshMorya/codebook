# Generated by Django 4.0.4 on 2022-05-10 10:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codebook_posts', '0013_delete_post_image_delete_post_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 10, 10, 4, 9, 764855, tzinfo=utc)),
        ),
    ]
