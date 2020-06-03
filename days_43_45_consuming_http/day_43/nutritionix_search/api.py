import requests
from collections import namedtuple
from operator import attrgetter
from typing import List
import secrets


Food = namedtuple('Food', 'brand_name, brand_name_item_name, brand_type, '
                          'food_name, locale, nf_calories, nix_brand_id, '
                          'nix_item_id, photo, region, serving_qty, serving_unit')


API_HEADERS = {'x-app-id': secrets.APPLICATION_ID, 'x-app-key': secrets.APPLICATION_KEY, 'x-remote-user-id': '0'}

API_URL = f'https://trackapi.nutritionix.com/v2/search/instant'


def find_branded_food_by_keyword(keyword: str) -> List[Food]:
    results = requests.get(f'{API_URL}?query={keyword}', headers=API_HEADERS)
    results.raise_for_status()
    results = results.json()

    branded_food = [Food(**f) for f in results.get('branded')]
    sorted_by_cals = sorted(branded_food, key=attrgetter('nf_calories'), reverse=True)[:10]
    return sorted_by_cals
