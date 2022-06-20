# Generated by Django 4.0.4 on 2022-04-29 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codebook_user', '0003_remove_user_id_alter_user_profile_pic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.CharField(blank=True, default='its my about section', max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='images/profile_pic_default.png', upload_to='images/'),
        ),
    ]