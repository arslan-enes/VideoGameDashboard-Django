from django.db import models

class VideoGame(models.Model):
    title = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    release_date = models.DateField()
    metascore = models.FloatField()
    user_score = models.FloatField()
    metascore_count = models.IntegerField()
    user_rating_count = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    summary = models.TextField()
    critic_reviews = models.TextField()

    def __str__(self):
        return self.title

