# Generated by Django 3.1.7 on 2021-04-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaUser_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='images/pawsse_paw.png', null=True, upload_to='images/'),
        ),
    ]
