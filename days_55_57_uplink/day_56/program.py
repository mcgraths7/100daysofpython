from api import MovieClient
from pprint import pprint


def main():
    input_loop()


def input_loop():
    while True:
        val = input("What kind of search would you like to perform? "
                    "Options are [k]eyword, [d]irector, or [i]mdb code. Alternatively, you may type 'x' to exit.\n>>> ")
        if not val:
            raise ValueError("Must specify a search type.")
        if val == 'x':
            return
        if val not in ['k', 'd', 'i']:
            raise ValueError("Invalid input.")

        try:
            if val == 'k':
                keyword = input("Please enter keyword\n>>> ").strip()
                get_movies_by_keyword(keyword)
            elif val == 'd':
                pass
            elif val == 'i':
                pass
        except ValueError as ve:
            print(ve)
            continue


def get_movies_by_keyword(keyword):
    svc = MovieClient()
    response = svc.find_by_keyword(keyword)
    movies = response.json().get('hits')

    print(f"Keyword {keyword} returned {len(movies)} results.")
    for idx, movie in enumerate(movies, 1):
        print(f"{idx}. {movie.get('title')} - {movie.get('year')}, directed by {movie.get('director')}")

    selected = get_movie_selection(movies)

    try:
        selected_movie = movies[selected - 1]
        pprint(selected_movie)
    except ValueError as ve:
        print(ve)
    get_movies_by_keyword(keyword)


def get_movie_selection(movies):
    selected = input(f"Please select one you'd like to see more info about, or enter 'x' to exit this search\n>>>")
    if selected == 'x':
        main()
    if not selected:
        raise ValueError("Must specify a number")
    elif not selected.isdigit():
        raise ValueError("Input must be a number.")
    elif int(selected) - 1 not in range(0, len(movies)):
        raise ValueError("Number must be within range of movies")
    else:
        return int(selected)
    # try:
    #     selected_movie = movies[selected - 1]
    #     pprint(selected_movie)
    #     get_movies_by_keyword(keyword)
    # except ValueError as ve:
    #     print(ve)


def get_movies_by_director(director):
    svc = MovieClient()


def get_movie_by_imdb_code(imdb_code):
    svc = MovieClient()


if __name__ == '__main__':
    main()
