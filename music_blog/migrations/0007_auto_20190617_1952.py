# Generated by Django 2.2.1 on 2019-06-17 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_blog', '0006_auto_20190617_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='composer',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='music_blog/composer_pics'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='music_blog/profile_pics'),
        ),
    ]
