# Generated by Django 4.0.4 on 2022-05-10 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codebook_user', '0009_alter_user_model_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='profile_pic',
            field=models.ImageField(default='images/profile_pic_default.png', upload_to='images/'),
        ),
    ]
