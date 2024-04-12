from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    followers = models.ManyToManyField('auth.User', related_name='followed_artists', blank=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, blank=True)
    release_date = models.DateField()
    likers = models.ManyToManyField('auth.User', related_name='liked_albums', blank=True)
    followers = models.ManyToManyField('auth.User', related_name='followed_albums', blank=True)
    cover = models.ImageField(upload_to='album_covers/', blank=True)

    def __str__(self):
        return self.title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    duration_seconds = models.IntegerField()
    likers = models.ManyToManyField('auth.User', related_name='liked_songs', blank=True)

    def __str__(self):
        return self.title


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song, related_name='playlists', blank=True)

    def __str__(self):
        return self.name


class UserActivity(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} played {self.song.title} on {self.date}'


class UserLike(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} liked {self.song.title}'