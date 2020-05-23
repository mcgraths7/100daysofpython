import random
import math

from player import Player


THROW_DEFINITIONS = {
    'r': 'rock',
    'p': 'paper',
    'sc': 'scissors',
    'l': 'lizard',
    'sp': 'spock'
}

WINNING_THROWS = {
    'rock': [{'scissors': 'crushes'}, {'lizard': 'crushes'}],
    'paper': [{'rock': 'covers'}, {'spock': 'disproves'}],
    'scissors': [{'paper': 'cut'}, {'lizard': 'decapitate'}],
    'lizard': [{'paper': 'eats'}, {'spock': 'poisons'}],
    'spock': [{'rock': 'vaporizes'}, {'scissors': 'smashes'}]
}


def print_header():
    print('------------------------')
    print('- Rock Paper Scissors Lizard Spock! -')


def get_number_of_rounds():
    num_rounds = input('3, 5, or 7 round match?: ')
    if num_rounds not in ['3', '5', '7']:
        print('Invalid input. Please select 3, 5, or 7 round match: ')
        get_number_of_rounds()
    else:
        return int(num_rounds)


def get_current_throw():
    inp = input('Please choose your throw: [r]ock, [p]aper, [sc]issors, [l]izard, or [sp]ock: ')
    if inp in THROW_DEFINITIONS.keys():
        return THROW_DEFINITIONS.get(inp)
    elif inp in THROW_DEFINITIONS.values():
        return inp


def get_winning_text(player_throw: str, cpu_throw: str):
    win = [winning_throw[cpu_throw] for winning_throw in WINNING_THROWS[player_throw] if cpu_throw in winning_throw.keys()]
    lose = [losing_throw[player_throw] for losing_throw in WINNING_THROWS[cpu_throw] if player_throw in losing_throw.keys()]
    return win, lose


def check_if_victory(player1, player2, rounds_to_win):
    if player1.rounds_won == rounds_to_win:
        print(f"You've won {rounds_to_win} rounds! You've won the match!")
        return True
    elif player2.rounds_won == rounds_to_win:
        print(f"Your opponent has won {rounds_to_win} rounds. You've lost the match")
        return True
    else:
        return False


def game_loop(player1: Player, player2: Player, num_rounds: int):
    current_round = 1
    rounds_to_win = math.floor((num_rounds / 2) + 1)
    print(f"First to {rounds_to_win} wins!")
    while current_round <= num_rounds:
        player_throw = None
        print(f"Round {current_round}... Throw!\n")
        try:
            player_throw = get_current_throw()
        except ValueError as ve:
            print(ve)
            continue
        cpu_throw = random.choice(list(THROW_DEFINITIONS.values()))

        print(f"You chose {player_throw}")
        print(f"Your opponent chose {cpu_throw}")

        winning_text = get_winning_text(player_throw, cpu_throw)

        if winning_text[0] and not winning_text[1]:
            print(f"Your {player_throw} {winning_text[0][0]} opponent's {cpu_throw}."
                  f" You've won this round!")
            player1.rounds_won += 1
            current_round += 1
        elif winning_text[1] and not winning_text[0]:
            print(f"Your opponent's {cpu_throw} {winning_text[1][0]} your {player_throw}. "
                  f"Unfortunately you've lost this round!")
            player2.rounds_won += 1
            current_round += 1
        elif not winning_text[0] and not winning_text[1]:
            print("It's a tie, throw again!")
            continue
        else:
            print("Something went wrong... Next round!")
            continue

        if check_if_victory(player1, player2, rounds_to_win):
            break
        else:
            print(f"The current score is {player1.rounds_won} to {player2.rounds_won}. On to round {current_round}")
            continue


def main():
    print_header()
    num_rounds = get_number_of_rounds()

    player_name = input("Please input your name: ")
    player1 = Player(name=player_name)
    player2 = Player(name='cpu')

    print(f"{player1.name} vs. {player2.name}. Best out of {num_rounds} rounds wins!")
    game_loop(player1, player2, num_rounds)


if __name__ == '__main__':
    main()