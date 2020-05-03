
class Throw:
    def __init__(self, name: str):
        self.name = name
        self.wins_against = []
        self.loses_against = []
        if self.name == 'rock':
            self.wins_against.append({'scissors': 'crushes'})
            self.wins_against.append({'lizard': 'crushes'})
            self.loses_against.append({'paper': 'covers'})
            self.loses_against.append({'spock': 'vaporizes'})
        elif self.name == 'paper':
            self.wins_against.append({'rock': 'covers'})
            self.wins_against.append({'spock': 'disproves'})
            self.loses_against.append({'scissors': 'cut'})
            self.loses_against.append({'lizard': 'eats'})
        elif self.name == 'scissors':
            self.wins_against.append({'paper': 'cut'})
            self.wins_against.append({'lizard': 'decapitate'})
            self.loses_against.append({'spock': 'smashes'})
            self.loses_against.append(({'rock': 'crushes'}))
        elif self.name == 'lizard':
            self.wins_against.append({'paper': 'eats'})
            self.wins_against.append({'spock': 'poisons'})
            self.loses_against.append({'rock': 'crushes'})
            self.loses_against.append({'scissors': 'decapitates'})
        elif self.name == 'spock':
            self.wins_against.append({'rock': 'vaporizes'})
            self.wins_against.append({'scissors': 'smashes'})
            self.loses_against.append({'lizard': 'poisons'})
            self.loses_against.append({'paper': 'disproves'})

    def get_winning_throws(self):
        return self.wins_against

    def get_losing_throws(self):
        return self.loses_against
