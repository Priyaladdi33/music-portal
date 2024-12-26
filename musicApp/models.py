from django.db import models

class Song(models.Model):
    name=models.CharField(max_length=255)
    singer=models.CharField(max_length=255)
    tags=models.CharField(max_length=100)
    image=models.FileField(upload_to='images/')
    song_file = models.FileField(upload_to='songs/', null=True, blank=True)

def __str__(self):
   return self.name
