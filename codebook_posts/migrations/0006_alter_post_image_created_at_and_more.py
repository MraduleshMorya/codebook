# Generated by Django 4.0.4 on 2022-05-05 12:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codebook_posts', '0005_alter_post_image_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_image',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 12, 13, 56, 524030, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post_text',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 12, 13, 56, 524975, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post_videos',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 12, 13, 56, 524586, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 12, 13, 56, 525442, tzinfo=utc)),
        ),
    ]
