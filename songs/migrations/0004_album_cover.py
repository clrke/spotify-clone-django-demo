# Generated by Django 4.2.11 on 2024-03-16 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_userlike_useractivity_playlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, upload_to='album_covers/'),
        ),
    ]
