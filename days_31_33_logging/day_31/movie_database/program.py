import sys
import requests.exceptions
import logbook

import api

logbook.set_datetime_format("local")

app_log = logbook.Logger('Application')


def main():
    keyword = input('Keyword of title search: ')

    try:
        results = api.find_movie_by_title(keyword)
        print(f'There are {len(results)} movies found.')
        for r in results:
            print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")
    except ValueError:
        msg = "Oops! You need to specify a search term!"
        print(msg)
        app_log.warn(msg)
    except requests.exceptions.ConnectionError:
        msg = "Unable to connect to the movie database server. Please check your network connection."
        print(msg)
        app_log.warn(msg)
    except Exception as x:
        msg = f"Oops, that didn't work! {x}"
        print(msg)
        app_log.exception(x)
    # Errors must go from most specific to most general, just like an if else block


def init_logging(filename: str = None):
    level = logbook.TRACE
    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()

    msg = f'Logging initialized, level: {level}, mode: {"stdout mode" if not filename else "file mode: " + filename}'
    logger = logbook.Logger('Startup')
    logger.notice(msg)


if __name__ == '__main__':
    init_logging('movie-app.log')
    main()
