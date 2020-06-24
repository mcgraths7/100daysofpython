import uplink
import requests


from uplink_helpers import raise_for_status


@raise_for_status
@uplink.json
class MovieClient(uplink.Consumer):
    def __init__(self):
        super().__init__(base_url="http://movie_service.talkpython.fm")

    @uplink.get('/api/search/{keyword}')
    def find_by_keyword(self, keyword) -> requests.models.Response:
        """Gets list of movies which contain the keyword"""

    @uplink.get('/api/director/{director_name}')
    def find_by_director(self, director_name) -> requests.models.Response:
        """Gets list of directors matching 'director_name' query"""

    @uplink.get('/api/movie/{imdb_code}')
    def find_by_imdb_code(self, imdb_code) -> requests.models.Response:
        """Gets list of movies with matching imdb code"""
