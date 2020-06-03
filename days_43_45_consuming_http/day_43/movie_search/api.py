from typing import List
from collections import namedtuple
import requests


Movie = namedtuple('Movie', 'imdb_code, title, director, keywords, '
                            'duration, genres, rating, year, imdb_score')

API_URL = 'https://movieservice.talkpython.fm/api/search'


def find_movie_by_keyword(keyword: str) -> List[Movie]:
    url = f'{API_URL}/{keyword}'

    resp = requests.get(url)
    resp.raise_for_status()
    resp = resp.json()

    movies = [Movie(**r) for r in resp.get('hits')]

    return movies
