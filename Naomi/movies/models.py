from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    director= models.CharField(max_length=100 , null=True, blank=True)
    sinopsis= models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
