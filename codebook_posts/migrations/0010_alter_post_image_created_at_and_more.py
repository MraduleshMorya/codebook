# Generated by Django 4.0.4 on 2022-05-09 06:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codebook_posts', '0009_alter_post_image_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_image',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 9, 6, 27, 6, 790704, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post_text',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 9, 6, 27, 6, 791659, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post_videos',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 9, 6, 27, 6, 791289, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 9, 6, 27, 6, 792158, tzinfo=utc)),
        ),
    ]