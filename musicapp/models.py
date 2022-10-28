
from django.db import models


# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name


class Song(models.Model):

    title = models.CharField(max_length=50)
    date_released = models.DateField()
    likes = models.PositiveIntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Lyric(models.Model):

    content = models.TextField(max_length=200)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        if len(self.content) > 50:
            return f"{self.content[0:50]}..."
        else:
            return f"{self.content}"
