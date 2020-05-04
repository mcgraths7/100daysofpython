import random
import math


from days_13_15.day_15.player import Player
from days_13_15.day_15.throw import Throw


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
    throw_name = input('Please choose your throw: [r]ock, [p]aper, [s]cissors, [l]izard, or [sp]ock: ')
    if throw_name not in ['r', 'rock', 'p', 'paper', 's', 'scissors', 'l', 'lizard', 'sp', 'spock']:
        raise ValueError('Invalid input, please try again.')
    return throw_name


def get_winning_text(throw1: Throw, throw2: Throw):
    winning_throws = throw1.get_winning_throws()
    losing_throws = throw1.get_losing_throws()
    for winning_throw in winning_throws:
        if throw2.name in winning_throw.keys():
            return {'victory': True, 'text': winning_throw[throw2.name]}
    for losing_throw in losing_throws:
        if throw2.name in losing_throw.keys():
            return {'victory': False, 'text': losing_throw[throw2.name]}
    return {'victory': False, 'text': None}


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
            elif player_input == 'l' or player_input == 'lizard':
                player_throw = Throw(name='lizard')
            elif player_input == 'sp' or player_input == 'spock':
                player_throw = Throw(name='spock')
        except ValueError as ve:
            print(ve)
            continue
        cpu_throw = Throw(random.choice(possible_throws))
        winning_throws = player_throw.get_winning_throws()
        print(f"You chose {player_throw.name}")
        print(f"Your opponent chose {cpu_throw.name}")

        winning_text = get_winning_text(player_throw, cpu_throw)
        if not winning_text['victory'] and winning_text['text'] is None:
            print("It's a tie! Throw again")
            continue
        elif winning_text['victory']:
            print(f"Your {player_throw.name} {winning_text['text']} opponent's {cpu_throw.name}."
                  f" You've won this round!")
            player1.rounds_won += 1
            current_round += 1
        elif not winning_text['victory']:
            print(f"Your opponent's {cpu_throw.name} {winning_text['text']} your {player_throw.name}. "
                  f"Unfortunately you've lost this round!")
            player2.rounds_won += 1
            current_round += 1

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
    possible_throws = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    player_name = input("Please input your name: ")
    player1 = Player(name=player_name)
    player2 = Player(name='cpu')

    print(f"{player1.name} vs. {player2.name}. Best out of {num_rounds} rounds wins!")
    game_loop(player1, player2, num_rounds, possible_throws)


if __name__ == '__main__':
    main()