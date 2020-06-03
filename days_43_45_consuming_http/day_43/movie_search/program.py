import api


def main():
    keyword = input('Please enter a keyword to search for: ')
    _find_movies_by_keyword(keyword)


def _find_movies_by_keyword(keyword: str):
    movies = api.find_movie_by_keyword(keyword)
    print(f"There were {len(movies)} results for {keyword}...")
    for idx, movie in enumerate(movies, 1):
        print(f"{idx}. {movie.title} ({movie.year}) -- {movie.imdb_score}")


if __name__ == '__main__':
    main()