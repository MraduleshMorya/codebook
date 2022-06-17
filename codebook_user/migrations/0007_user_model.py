# Generated by Django 4.0.4 on 2022-05-10 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codebook_user', '0006_alter_friends2_temp'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_model',
            fields=[
                ('username', models.CharField(max_length=150, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('phone_no', models.CharField(max_length=10, unique=True)),
                ('profile_pic', models.ImageField(default='media/images/profile_pic_default.png', upload_to='images/')),
                ('birth_date', models.DateField()),
                ('about', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
