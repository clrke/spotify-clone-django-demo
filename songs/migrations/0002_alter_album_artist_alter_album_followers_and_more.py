# Generated by Django 4.2.11 on 2024-03-16 03:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='songs.artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followed_albums', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='album',
            name='likers',
            field=models.ManyToManyField(blank=True, related_name='liked_albums', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='artist',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followed_artists', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='songs.album'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='songs.artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='likers',
            field=models.ManyToManyField(blank=True, related_name='liked_songs', to=settings.AUTH_USER_MODEL),
        ),
    ]