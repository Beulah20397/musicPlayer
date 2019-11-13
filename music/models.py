from django.db import models
from django.urls import reverse

class Album(models.Model):
    name = models.CharField(max_length=250)
    albumTitle = models.CharField(max_length=500)
    genre = models.CharField(max_length=1000)
    albumLogo = models.FileField(default=False)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.albumTitle + '-' + self.name

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    fileType = models.CharField(max_length=10)
    songTitle = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.songTitle

class Musicians(models.Model):
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    gender = models.CharField(max_length=10)
    educationQualifications = models.CharField(max_length=1000)