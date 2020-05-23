
class Throw:
    def __init__(self, name: str):
        self.name = name
        if self.name == 'rock':
            self.wins_against = 'scissors'
            self.loses_against = 'paper'
        elif self.name == 'paper':
            self.wins_against = 'rock'
            self.loses_against = 'scissors'
        elif self.name == 'scissors':
            self.wins_against = 'paper'
            self.loses_against = 'rock'
