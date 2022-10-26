from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)

    def _str_(self):
        return self.first_name

class Song(models.Model):
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    date_released = models.CharField(max_length=50)
    likes = models.CharField(max_length=50)
    artisteid = models.CharField(max_length=50)


class Lyric(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=5000)
    songid = models.CharField(max_length=50)


