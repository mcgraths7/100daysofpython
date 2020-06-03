import api
from pprint import pprint


def main():

    keyword = input('Enter a keyword to search for in the Nutritionix database... ')
    res = api.find_branded_food_by_keyword(keyword)
    for idx, f in enumerate(res, 1):
        print(f"{idx}. {f.brand_name} - {f.brand_name_item_name} ({f.nf_calories} cal per "
              f"{f.serving_qty} {f.serving_unit})")


if __name__ == '__main__':
    main()