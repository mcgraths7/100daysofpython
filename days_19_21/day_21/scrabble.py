import itertools
import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
LETTER_VALUES = {
    1: 'A E I O U L N S T R',
    2: 'D G',
    3: 'B C M P',
    4: 'F H V W Y',
    5: 'K',
    8: 'J X',
    10: 'Q Z'
}
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_max_word_value(draw):
    current_max_value = 0
    max_value_word = ""
    words = _get_possible_dict_words(draw)
    for word in words:
        value = _get_word_value(word)
        if value > current_max_value:
            current_max_value = value
            max_value_word = word
    return {'word': max_value_word, 'value': current_max_value}


# Below are helper methods

def _get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    permutations = _get_permutations_draw(draw)
    return [word.lower() for word in permutations if word.lower() in dictionary]
    pass


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    one_letter = ["".join(comb) for comb in list(itertools.permutations(draw, 1))]
    two_letter = ["".join(comb) for comb in list(itertools.permutations(draw, 2))]
    three_letter = ["".join(comb) for comb in list(itertools.permutations(draw, 3))]
    four_letter = ["".join(comb) for comb in list(itertools.permutations(draw, 4))]
    five_letter = ["".join(comb) for comb in list(itertools.permutations(draw, 5))]
    six_letter = ["".join(comb) for comb in list(itertools.permutations(draw, 6))]
    seven_letter = ["".join(comb) for comb in list(itertools.permutations(draw, 7))]
    perms = []
    for n in range(1, 8):
        perms = perms + _get_permutations_n_letters(draw, n)
    return perms
    pass


def _get_letter_value(letter):
    for value, letters in LETTER_VALUES.items():
        if letter.upper() in letters.split():
            return value


def _get_word_value(word):
    total_value = 0
    for letter in list(word):
        value = _get_letter_value(letter)
        total_value += value
    return total_value


def _get_permutations_n_letters(draw, n):
    return ["".join(comb) for comb in list(itertools.permutations(draw, n))]


print(get_max_word_value(['A', 'E' 'B', 'Y', 'P', 'D', 'M']))