from django.db import models
from movies_api.form_options import GENRE_OPTIONS, STUDIO_OPTIONS, ACTORS_OPTIONS


class Movies(models.Model):
    name = models.CharField(max_length=55, default='')
    genre = models.CharField(default='', max_length=50, choices=GENRE_OPTIONS)
    studio = models.CharField(default='', max_length=50, choices=STUDIO_OPTIONS)
    actors = models.CharField(default='', max_length=50, choices=ACTORS_OPTIONS)
    imdb = models.FloatField(default=0.0)

    metascore = models.IntegerField(default=0)
    user_score = models.FloatField(default=0.0)

    tomatometer = models.IntegerField(default=0)
    audience_score = models.IntegerField(default=0)

    liked_this_film = models.IntegerField(default=0)
    audience_rating_summary = models.FloatField(default=0.0)

    budget = models.FloatField(default=0.0)
    box_office = models.FloatField(default=0.0)

    def __str__(self):
        return self.genre, self.studio, self.actors
