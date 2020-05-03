import random
import math


from days_13_15.day_14.player import Player
from days_13_15.day_14.throw import Throw


def print_header():
    print('------------------------')
    print('- Rock Paper Scissors! -')


def get_number_of_rounds():
    num_rounds = input('3, 5, or 7 round match?: ')
    if num_rounds not in ['3', '5', '7']:
        print('Invalid input. Please select 3, 5, or 7 round match: ')
        get_number_of_rounds()
    else:
        return int(num_rounds)


def get_current_throw():
    throw_name = input('Please choose your throw: [r]ock, [p]aper, or [s]cissors: ')
    if throw_name not in ['r', 'rock', 'p', 'paper', 's', 'scissors']:
        raise ValueError('Invalid input, please try again.')
    return throw_name


def game_loop(player1: Player, player2: Player, num_rounds: int, possible_throws: list):
    current_round = 1
    rounds_to_win = math.floor((num_rounds / 2) + 1)
    print(f"First to {rounds_to_win} wins!")
    while current_round <= num_rounds:
        player_throw = None
        print(f"Round {current_round}... Throw!\n")
        try:
            player_input = get_current_throw()
            if player_input == 'r' or player_input == 'rock':
                player_throw = Throw(name='rock')
            elif player_input == 'p' or player_input == 'paper':
                player_throw = Throw(name='paper')
            elif player_input == 's' or player_input == 'scissors':
                player_throw = Throw(name='scissors')
        except ValueError as ve:
            print(ve)
            continue
        cpu_throw = Throw(random.choice(possible_throws))
        print(f"You chose {player_throw.name}")
        print(f"Your opponent chose {cpu_throw.name}")
        if player_throw.wins_against == cpu_throw.name:
            print(f"Your {player_throw.name} beats {cpu_throw.name}. You've won this round!")
            player1.rounds_won += 1
            current_round += 1
        elif player_throw.loses_against == cpu_throw.name:
            print(f"Your opponents {cpu_throw.name} beats your {player_throw.name}. "
                  f"Unfortunately you've lose this round!")
            player2.rounds_won += 1
            current_round += 1
        else:
            print("It's a tie! Throw again.")
            continue

        if player1.rounds_won == rounds_to_win:
            print(f"You've won {rounds_to_win} rounds! You've won the match!")
            break
        elif player2.rounds_won == rounds_to_win:
            print(f"Your opponent has won {rounds_to_win} rounds. You've lost the match")
            break
        else:
            print(f"The current score is {player1.rounds_won} to {player2.rounds_won}. On to round {current_round}")


def main():
    print_header()
    num_rounds = get_number_of_rounds()
    possible_throws = ['rock', 'paper', 'scissors']

    player_name = input("Please input your name: ")
    player1 = Player(name=player_name)
    player2 = Player(name='cpu')

    print(f"{player1.name} vs. {player2.name}. Best out of {num_rounds} rounds wins!")
    game_loop(player1, player2, num_rounds, possible_throws)


if __name__ == '__main__':
    main()