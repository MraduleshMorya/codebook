# Generated by Django 4.0.4 on 2022-04-28 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=10, unique=True)),
                ('profile_pic', models.ImageField(upload_to='images/')),
                ('birth_date', models.DateField()),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='codebook_user.user')),
            ],
        ),
    ]
