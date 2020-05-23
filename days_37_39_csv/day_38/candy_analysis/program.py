import research


class CandyMatcher:

    def __init__(self):
        self.categories = []
        self.matched_candy = []

    def print_header():
        print("Welcome to the Candy Matcher! We'll ask preferences and generate a list of candy you might like!")
        print("=======================")

    def __call__(self):
        research.init()
        matched_candy = []
        while True:
            inp = input(
                "Please enter, one category at a time, what kind of candy you like (pick from: chocolate, fruity,"
                "caramel, peanutyalmondy, nougat, crispedricewafer, hard, bar. Type 'f' when finished.\n>>> ")

            try:
                if self._check_input(inp) is 'f':
                    break
            except ValueError as ve:
                print(ve)
                continue
        self._get_matched_candy()

        while True:
            inp = input("Do you prefer [single] candy, or when [multiple] come in a package?")
            if self._check_input(inp) == 'single':
                try:
                    self.categories.append('pluribus')
                except ValueError as ve:
                    print(ve)
                    continue
            self._get_matched_candy()
        print(self.matched_candy)

    def _get_matched_candy(self):
        for idx, cat in enumerate(self.categories):
            if idx == 0:
                self.matched_candy = research.get_candy_by_descriptor(cat)
            else:
                self.matched_candy = research.get_candy_by_descriptor(cat, self.matched_candy)
        return self.matched_candy

    def _check_input(self, inp):
        if inp == 'f':
            return 'f'
        if not inp:
            raise ValueError("You need to specify a category. Please select from one of the available categories.")
        if inp not in ['chocolate', 'fruity', 'caramel', 'peanutyalmondy', 'nougat', 'crispedricewafer', 'hard',
                               'bar']:
            raise ValueError("I didn't quite get that. Please select from one of the available categories.")
        if inp in self.categories:
            raise ValueError(f"You've already selected {inp}, please try another category")
        self.categories.append(inp)
        return inp


if __name__ == '__main__':
    cm = CandyMatcher()
    cm()

# TODO: Fix second round of questions (single or multiple items)