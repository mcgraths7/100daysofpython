import os
import csv
from collections import namedtuple
from typing import List

data = []

Record = namedtuple(
    'Record',
    'date,actual_mean_temp,actual_min_temp,actual_max_temp,average_min_temp,'
    'average_max_temp,record_min_temp,record_max_temp,record_min_temp_year,'
    'record_max_temp_year,actual_precipitation,average_precipitation,'
    'record_precipitation'
)


def init(filename):
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', filename)

    with open(filename, 'r', encoding='utf-8') as fn:
        reader = csv.DictReader(fn)
        data.clear()
        for row in reader:
            r = create_record_from_row(row)
            data.append(r)


def create_record_from_row(row):
    # date,actual_mean_temp,actual_min_temp,actual_max_temp,
    # average_min_temp,average_max_temp,record_min_temp,record_max_temp,
    # record_min_temp_year,record_max_temp_year,actual_precipitation,
    # average_precipitation,record_precipitation
    # date, int x 9, float x 3

    row['actual_mean_temp'] = int(row['actual_mean_temp'])
    row['actual_min_temp'] = int(row['actual_min_temp'])
    row['actual_max_temp'] = int(row['actual_max_temp'])
    row['average_min_temp'] = int(row['average_min_temp'])
    row['average_max_temp'] = int(row['average_max_temp'])
    row['record_min_temp'] = int(row['record_min_temp'])
    row['record_max_temp'] = int(row['record_max_temp'])
    row['record_min_temp_year'] = int(row['record_min_temp_year'])
    row['record_max_temp_year'] = int(row['record_max_temp_year'])
    row['actual_precipitation'] = float(row['actual_precipitation'])
    row['average_precipitation'] = float(row['average_precipitation'])
    row['record_precipitation'] = float(row['record_precipitation'])

    r = Record(
        **row
    )
    return r


def hot_days() -> List[Record]:
    return sorted(data, key=lambda r: r.actual_max_temp, reverse=True)


def cold_days() -> List[Record]:
    return sorted(data, key=lambda r: r.actual_min_temp)


def wettest_days() -> List[Record]:
    return sorted(data, key=lambda r: r.actual_precipitation, reverse=True)

