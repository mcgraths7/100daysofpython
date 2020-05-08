import itertools
import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
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


def _get_permutations_n_letters(draw, n):
    return ["".join(comb) for comb in list(itertools.permutations(draw, n))]
