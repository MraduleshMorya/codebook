# Generated by Django 4.0.4 on 2022-05-05 11:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codebook_posts', '0002_alter_post_image_created_at_alter_post_image_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='post_text',
            fields=[
                ('username', models.CharField(max_length=150)),
                ('postid', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 5, 5, 11, 3, 9, 630739, tzinfo=utc))),
                ('description', models.TextField(max_length=1500)),
                ('catagory', models.CharField(default='text', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='post_videos',
            fields=[
                ('username', models.CharField(max_length=150)),
                ('postid', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('video', models.FileField(upload_to='posted_videos/')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 5, 5, 11, 3, 9, 630381, tzinfo=utc))),
                ('description', models.CharField(max_length=1000)),
                ('catagory', models.CharField(default='video', max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name='post_image',
            name='catagory',
            field=models.CharField(default='image', max_length=6),
        ),
        migrations.AlterField(
            model_name='post_image',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 11, 3, 9, 629804, tzinfo=utc)),
        ),
    ]