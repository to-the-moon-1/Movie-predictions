# Generated by Django 4.1.6 on 2023-02-13 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_api', '0002_movies_actors_movies_genre_movies_studio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='imbd',
            new_name='imdb',
        ),
    ]
