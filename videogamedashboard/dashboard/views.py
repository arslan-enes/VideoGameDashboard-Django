from django.shortcuts import render
from .models import VideoGame
import pandas as pd

def bar(request):

    games = VideoGame.objects.all()

    games = pd.DataFrame(games.values())
    
    genres = ["Action", "Adventure", "Puzzle", "Racing", "Role-Playing"]

    genre_counts = {}
 
    for genre in genres:
        genre_counts[genre] = games[games["genres"].str.contains(genre)].shape[0]


    return render(request, "dashboard/bar.html", {"genre_counts_dict":  genre_counts,
                                                  "genre_counts":       list(genre_counts.values()),
                                                  "genres":        list(genre_counts.keys())})