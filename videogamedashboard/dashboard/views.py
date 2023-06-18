from django.shortcuts import render
from django.http import JsonResponse
from .models import VideoGame
import pandas as pd

games = VideoGame.objects.all()
games = pd.DataFrame(games.values())

def bar(request):

    
    genres = ["Action", "Adventure", "Puzzle", "Racing", "Role-Playing", "Platformer", "Shooter", "First-Person", "Open-World"]

    genre_counts = {}
 
    for genre in genres:
        genre_counts[genre] = games[games["genres"].str.contains(genre)].shape[0]

    return render(request, "dashboard/bar.html", {"genre_counts_dict":  genre_counts,
                                                  "genre_counts":       list(genre_counts.values()),
                                                  "genres":        list(genre_counts.keys())})

def scatter_data(request):

    data = games.sort_values(by=["metascore", "user_score"], ascending=False)[["title", "metascore", "user_score"]].dropna()
    data = data.sample(50)
    label = data["title"].to_list()
    data = data.drop(columns=["title"])
    data["user_score"] = data["user_score"] * 10
    data = data.rename(columns={"metascore": "x", "user_score": "y"})
    data = data.to_dict(orient="records")

    labels = label
    datasets = [
        {
            'label': 'PC Games',
            'data': data,
            'backgroundColor': 'rgba(255, 99, 132, 0.5)'  # Set color if needed
        }
    ]

    data = {
        'labels': labels,
        'datasets': datasets
    }

    return JsonResponse(data)


def scatter(request):
    return render(request, "dashboard/scatter.html")