import research


class CandyMatcher:

    def __init__(self):
        self.categories = []
        self.matched_candy = []

    def print_header(self):
        print("Welcome to the Candy Matcher! We'll ask preferences and generate a list of candy you might like!")
        print("=======================")

    def __call__(self):
        research.init()
        matched_candy = []

        while True:
            inp = input(
                "Please enter, one category at a time, what kind of candy you like (pick from: chocolate, fruity, "
                "caramel, peanutyalmondy, nougat, crispedricewafer, hard, bar. Type 'f' when finished.\n>>> ")

            try:
                if self._check_first_input(inp) is 'f':
                    break
            except ValueError as ve:
                print(ve)
                continue
            self._get_matched_candy()

        while True:
            inp = input("Do you prefer [single] candies, or ones that include [multiple] in one package?\n>>> ")
            try:
                if self._check_second_input(inp):
                    print(self.matched_candy)
                    self._get_matched_candy()
                    break
            except ValueError as ve:
                print(ve)
                continue


        sorted_candy = research.sort_matched_candy_by('winpercent', self.matched_candy)
        top_five = research.get_top_five_candy(sorted_candy)

        if top_five:
            print("Below is a list of the top matching candies, based on your selections:")
            for idx, candy in enumerate(top_five, 1):
                print(f"{idx}. {candy.competitorname}")
        else:
            print("Unfortunately, it seems no candy in our database matches your preference.")

    def _get_matched_candy(self):
        # TODO: try to consolidate into list comprehension
        for idx, cat in enumerate(self.categories):
            if idx == 0:
                self.matched_candy = research.get_candy_by_descriptor(cat)
            else:
                if cat == 'single':
                    self.matched_candy = research.get_candy_by_descriptor('pluribus', self.matched_candy, value=0)
                elif cat == 'multiple':
                    self.matched_candy = research.get_candy_by_descriptor('pluribus', self.matched_candy)
                else:
                    self.matched_candy = research.get_candy_by_descriptor(cat, self.matched_candy)
        return self.matched_candy

    def _check_first_input(self, inp):
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

    def _check_second_input(self, inp):
        if not inp:
            raise ValueError("You need to specify either single or multiple.")
        if inp not in ['single', 'multiple']:
            raise ValueError("I didn't quite get that. Please select either single or multiple.")
        self.categories.append(inp)
        return inp


if __name__ == '__main__':
    cm = CandyMatcher()
    cm()
