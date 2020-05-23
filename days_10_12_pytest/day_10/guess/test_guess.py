from unittest.mock import patch
import random
import pytest


from guess import get_random_number, Game


@patch.object(random, 'randint')
def test_get_random_number(m):
    m.return_value = 17
    assert get_random_number() == 17


@patch("builtins.input", side_effect=[1, '12', -1, 21, 'bob', '', None, 12])
def test_guess(inp):
    game = Game()
    # good inputs - 1, '12' ('12' gets converted to int)
    assert game.guess() == 1
    assert game.guess() == 12
    # not in range - '-1, 21'
    with pytest.raises(ValueError):
        game.guess()
    with pytest.raises(ValueError):
        game.guess()
    # Not a number - 'bob', '', None
    with pytest.raises(ValueError):
        game.guess()
    with pytest.raises(ValueError):
        game.guess()
    with pytest.raises(ValueError):
        game.guess()
    # Already guessed - 12
    with pytest.raises(ValueError):
        game.guess()


def test_validate_guess(capfd):
    game = Game()
    game._answer = 2

    # Test incorrect values
    # Too low
    assert not game._validate_guess(1)
    out, _ = capfd.readouterr()
    assert out.strip() == '1 is too low'
    # Too low
    assert not game._validate_guess(3)
    out, _ = capfd.readouterr()
    assert out.strip() == '3 is too high'

    # Test correct values
    assert game._validate_guess(2)
    out, _ = capfd.readouterr()
    assert out.strip() == '2 is correct!'


@patch("builtins.input", side_effect=[1, 21, 19, 10, 14])
def test_game_win(inp, capfd):
    game = Game()
    game._answer = 14

    game()
    # Mock a game in which you win in 4 tries
    assert game._win == True
    assert len(game._guesses) == 4

    out = capfd.readouterr()[0]
    expected_output = ['1 is too low',
                       'Number not in range',
                       '19 is too high',
                       '10 is too low',
                       '14 is correct!',
                       'It took you 4 guesses']
    output = [line.strip() for line in out.split('\n') if line.strip()]
    assert output == expected_output


@patch("builtins.input", side_effect=[1, 8, 12, 12, 9, 11])
def test_game_lose(inp, capfd):
    game = Game()
    game._answer = 10

    game()
    # Mock a game in which you do not win, ie you expend your 5 guesses
    assert game._win == False
    assert len(game._guesses) == 5

    out = capfd.readouterr()[0]
    expected_output = ['1 is too low',
                       '8 is too low',
                       '12 is too high',
                       'Already guessed',
                       '9 is too low',
                       '11 is too high',
                       'Guessed 5 times, answer was 10']
    output = [line.strip() for line in out.split('\n') if line.strip()]
    assert output == expected_output
