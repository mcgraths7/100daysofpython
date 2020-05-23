CARS = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=None):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    if cars is None:
        cars = CARS
    return ', '.join([model for make, model in cars.items() if make == 'Jeep'][0])
    pass


def get_first_model_each_manufacturer(cars=None):
    """return a list of matching models (original ordering)"""
    if cars is None:
        cars = CARS
    first_models = [model for make, models in cars.items() for model in models if model == models[0]]
    return first_models
    pass


def get_all_matching_models(cars=None, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    if cars is None:
        cars = CARS
    matching_models = [model for make, models in cars.items() for model in models if grep.lower() in model.lower()]
    return sorted(matching_models)
    pass


def sort_car_models(cars=None):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""

    if cars is None:
        cars = CARS
    sorted_cars = [sorted(models) for make, models in cars.items()]
    return sorted_cars

    pass
