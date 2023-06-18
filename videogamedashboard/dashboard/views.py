from django.shortcuts import render
from .models import VideoGame
import pandas as pd

def bar(request):

    games = VideoGame.objects.all()

    games = pd.DataFrame(games.values())
    
    selected_genres = ["Action", "Adventure", "Puzzle", "Racing", "Role-Playing"]

    genre_counts = []

    for genre in selected_genres:
        genre_counts.append(games[games["genres"].str.contains(genre)].shape[0])

    print(selected_genres)
    print(genre_counts)


    return render(request, "dashboard/bar.html", {"genres": selected_genres, "genre_counts": genre_counts})