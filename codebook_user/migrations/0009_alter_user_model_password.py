# Generated by Django 4.0.4 on 2022-05-10 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codebook_user', '0008_alter_user_model_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
