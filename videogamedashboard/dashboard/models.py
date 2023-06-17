from django.db import models

class VideoGame(models.Model):
    title = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    release_date = models.DateField()
    metascore = models.FloatField(null=True, blank=True)
    user_score = models.FloatField(null=True, blank=True)
    metascore_count = models.IntegerField(null=True, blank=True)
    user_rating_count = models.IntegerField(null=True, blank=True)
    platform = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    summary = models.TextField(null=True, blank=True)
    critic_reviews = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

