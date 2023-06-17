from dashboard.models import VideoGame

game = VideoGame(
    title='The Witcher 3: Wild Hunt',
    publisher='CD Projekt Red',
    release_date='2015-05-19',
    metascore=93.0,
    user_score='NULL',
    metascore_count=81,
    user_rating_count=0,
    platform='PC',
    genres='Role-Playing, Action RPG',
    summary='',
    critic_reviews=''
)

game.save()