import csv
from namedlist import namedlist
from math import fsum


with open('movie_metadata.csv', mode='r', encoding='utf-8') as directors_csv:
    csv_reader = csv.DictReader(directors_csv, delimiter=",")
    line_count = 0
    Movie = namedlist('Movie', 'title year rating')
    Director = namedlist('Director', 'name movies average_rating')
    directors = {}
    for row in csv_reader:
        if line_count == 40:
            break
        elif line_count == 0:
            line_count += 1
        elif row['director_name'] is not '':
            line_count += 1
            m = Movie(title=row['movie_title'].strip(),
                          year=row['title_year'],
                          rating=row['imdb_score'])
            d = Director(name=row['director_name'],
                         movies=[],
                         average_rating=None)


def get_average_rating(director):
    scores = []
    for movie in director:
        scores.append(float(movie['rating']))
    return round((fsum(scores) / len(scores)), 2)


# def top_five_directors(dir_list):
#     averages = defaultdict(list)
#     Director = namedtuple('Director', 'name movies')
#     for director in dir_list.items():
#         d = Director(name=director[0], movies=director[1])
#         if len(d.movies) >= 4:
#             averages[d.name] = get_average_rating(d.movies)
#     return sorted(averages.items(), key=lambda x: x[1], reverse=True)[:5]
#
#
# def list_movies(dir_list):
#     for index, director in enumerate(dir_list, start=0):
#         print(f"{index + 1}. {director[0]}\t\t\t\t\t\t {director[1]}")
#
#
# list_movies(top_five_directors(directors))



# Potential refactor: use namedtuple for director as well

# elif row['director_name'] is not '':
# movie = Movie(title=row['movie_title'],
#               year='title_year',
#               rating=row['imdb_score'])
# director = Director(name=row['director_name'], movies=[])
# directors[director.name['movies']].append(movie)