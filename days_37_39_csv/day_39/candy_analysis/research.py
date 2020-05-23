import os
import csv
from collections import namedtuple
from operator import attrgetter
from typing import List

data = []
Candy = namedtuple('Candy', 'competitorname,chocolate,fruity,caramel,peanutyalmondy,'
                            'nougat,crispedricewafer,hard,bar,pluribus,sugarpercent,'
                            'pricepercent,winpercent')


def init():
    folder = os.path.dirname(__file__)
    file_path = os.path.join(folder, 'data', 'candy-data.csv')
    with open(file_path, 'r', encoding='utf-8') as f:
        data.clear()
        reader = csv.DictReader(f)
        for r in reader:
            c = create_candy_from_row(r)
            data.append(c)


def create_candy_from_row(row) -> Candy:
    # int x 8, float x 3
    row['chocolate'] = int(row['chocolate'])
    row['fruity'] = int(row['fruity'])
    row['caramel'] = int(row['caramel'])
    row['peanutyalmondy'] = int(row['peanutyalmondy'])
    row['nougat'] = int(row['nougat'])
    row['crispedricewafer'] = int(row['crispedricewafer'])
    row['hard'] = int(row['hard'])
    row['bar'] = int(row['bar'])
    row['pluribus'] = int(row['pluribus'])
    row['sugarpercent'] = float(row['sugarpercent'])
    row['pricepercent'] = float(row['pricepercent'])
    row['winpercent'] = float(row['winpercent'])

    c = Candy(
        **row
    )
    return c


def get_candy_by_descriptor(descriptor: str, candy_list=None, value=1) -> List[Candy]:
    if candy_list is None:
        candy_list = data
    return [candy for candy in candy_list if _convert_candy_to_dict(candy)[descriptor] == value]


def sort_matched_candy_by(sortable: str, matched_candy: List[Candy]) -> List[Candy]:
    return sorted(matched_candy, key=attrgetter(sortable), reverse=True)


def get_top_five_candy(matched_candy: List[Candy]) -> List[Candy]:
    return matched_candy[:5]

# Helper methods


def _convert_candy_to_dict(candy: Candy) -> dict:
    return candy._asdict()


