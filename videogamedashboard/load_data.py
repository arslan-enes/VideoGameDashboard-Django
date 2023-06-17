import pandas as pd
from dashboard.models import VideoGame

def load_data():
    df = pd.read_csv('MetacriticPCGamesofAllTime_cleaned.csv')
    df = df.where(pd.notnull(df), None)
    for index, row in df.iterrows():
        VideoGame.objects.create(
            title=row['title'],
            release_date=row['release_date'],
            metascore=row['metascore'],
            metascore_count=row['metascore_count'],
            user_score=row['user_score'],
            user_rating_count=row['user_rating_count'],
            critic_reviews=row['critic_reviews'],
            genres=row['genres'],
            publisher=row['publisher'],
            summary=row['summary'],
        )
