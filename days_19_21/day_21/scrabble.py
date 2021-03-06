import itertools
import os
import sys
import urllib.request
import logbook

scrabble_logs = logbook.Logger('Scrabble Helper')
logbook.set_datetime_format("local")


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
    if len(draw) > 7:
        raise ValueError('Too many letters')
    elif len(draw) == 0:
        raise ValueError('Need at least one letter')
    words = _get_possible_dict_words(draw)
    scrabble_logs.trace(f"Calculating max value word for draw {draw}")
    words_with_values = {word: _get_word_value(word) for word in words}
    try:

        max_value_word = max(words_with_values, key=lambda x: words_with_values[x])
        max_value = words_with_values[max_value_word]
        scrabble_logs.trace(f"The highest scoring word for draw {draw} is {max_value_word} "
                            f"worth {max_value} points")
        return {'word': max_value_word, 'value': max_value}
    except ValueError as ve:
        scrabble_logs.error("A problem occurred: " + str(ve))
        print(ve)


# Below are helper methods

def _get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    permutations = _get_permutations_draw(draw)
    scrabble_logs.trace(f"Getting possible dictionary words from permutations...")
    words = [word.lower() for word in permutations if word.lower() in dictionary]
    scrabble_logs.trace(f"Matched {len(words)} dictionary words.")
    return words
    pass


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    scrabble_logs.trace(f"Generating possible permutations for draw {draw}...")
    one_letter = ["".join(comb) for comb in list(itertools.permutations(draw, 1))]
    two_letter = ["".join(comb) for comb in list(itertools.permutations(draw, 2))]
    three_letter = ["".join(comb) for comb in list(itertools.permutations(draw, 3))]
    four_letter = ["".join(comb) for comb in list(itertools.permutations(draw, 4))]
    five_letter = ["".join(comb) for comb in list(itertools.permutations(draw, 5))]
    six_letter = ["".join(comb) for comb in list(itertools.permutations(draw, 6))]
    seven_letter = ["".join(comb) for comb in list(itertools.permutations(draw, 7))]
    perms = list(one_letter + two_letter + three_letter + four_letter + five_letter + six_letter + seven_letter)
    scrabble_logs.trace(f"{len(perms)} possible permutations.")
    return perms
    pass


def _get_letter_value(letter):
    return [value for value, letters in LETTER_VALUES.items() if letter.upper() in letters.split()][0]


def _get_word_value(word):
    return sum([_get_letter_value(letter) for letter in list(word)])


def _get_permutations_n_letters(draw, n):
    return ["".join(comb) for comb in list(itertools.permutations(draw, n))]


def init_logging(filename: str= None):
    level = logbook.TRACE
    if filename:
        logbook.TimedRotatingFileHandler(filename=filename, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()

    msg = f'Logging initialized, level: {level}, mode: {"stdout mode" if not filename else "file mode: " + filename}'
    logger = logbook.Logger('Startup')
    logger.notice(msg)


if __name__ == '__main__':
    init_logging(filename="scrabble.log")
    try:
        max_value = get_max_word_value(list(sys.argv[1]))
        print(max_value)
    except IndexError as ie:
        scrabble_logs.warn("Need to specify at least one letter")
        print("Need to specify at least one letter")
