# Generated by Django 4.0.4 on 2022-07-07 11:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('codebook_posts', '0050_alter_posts_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
