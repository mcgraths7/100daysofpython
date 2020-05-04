
class Throw:
    def __init__(self, name: str):
        self.name = name
        self.wins_against = []
        if self.name == 'rock':
            self.wins_against.append({'scissors': 'crushes'})
            self.wins_against.append({'lizard': 'crushes'})
        elif self.name == 'paper':
            self.wins_against.append({'rock': 'covers'})
            self.wins_against.append({'spock': 'disproves'})
        elif self.name == 'scissors':
            self.wins_against.append({'paper': 'cut'})
            self.wins_against.append({'lizard': 'decapitate'})
        elif self.name == 'lizard':
            self.wins_against.append({'paper': 'eats'})
            self.wins_against.append({'spock': 'poisons'})
        elif self.name == 'spock':
            self.wins_against.append({'rock': 'vaporizes'})
            self.wins_against.append({'scissors': 'smashes'})

    def get_winning_throws(self):
        return self.wins_against

    def get_losing_throws(self):
        return self.loses_against
