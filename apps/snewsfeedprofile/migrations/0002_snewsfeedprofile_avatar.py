# Generated by Django 3.1.7 on 2021-02-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snewsfeedprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snewsfeedprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
