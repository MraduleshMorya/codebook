# Generated by Django 4.0.4 on 2022-05-24 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codebook_user', '0012_post_commnets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends2',
            name='temp',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
