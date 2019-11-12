from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=500)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=10)
    albumTitle = models.CharField(max_length=500)
    genre = models.CharField(max_length=1000)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.albumTitle + '-' + self.name

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    fileType = models.CharField(max_length=10)
    songTitle = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.songTitle