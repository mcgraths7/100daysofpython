import requests.exceptions
import api


def main():
    keyword = input('Keyword of title search: ')

    try:
        results = api.find_movie_by_title(keyword)
        print(f'There are {len(results)} movies found.')
        for r in results:
            print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")
    except ValueError:
        print("Oops! You need to specify a search term!")
    except requests.exceptions.ConnectionError:
        print("Unable to connect to the movie database server. Please check your network connection.")
    except Exception as x:
        print(f'Oops, an error occurred: ', x)
    # Errors must go from most specific to most general, just like an if else block


if __name__ == '__main__':
    main()
