import research
import cProfile


profiler = cProfile.Profile()
profiler.disable()


class CandyMatcher:

    def __init__(self):
        self.categories = []
        self.matched_candy = []

    def print_header(self):
        print("Welcome to the Candy Matcher! We'll ask preferences and generate a list of candy you might like!")
        print("=======================")

    def __call__(self):
        profiler.enable()
        research.init()
        matched_candy = []

        while True:
            # inp = input(
            #     "Please enter, one category at a time, what kind of candy you like (pick from: chocolate, fruity, "
            #     "caramel, peanutyalmondy, nougat, crispedricewafer, hard, bar. Type 'f' when finished.\n>>> ")
            self.categories = ['chocolate', 'caramel']
            inp = 'f'

            try:
                if self._check_first_input(inp) is 'f':
                    break
            except ValueError as ve:
                print(ve)
                continue
            self._get_matched_candy()

        while True:
            inp = 'single' # using predefined values to eliminate input skew
            # inp = input("Do you prefer [single] candies, or ones that include [multiple] in one package?\n>>> ")
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
        profiler.disable()

    def _get_matched_candy(self):
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
    for _ in range(1, 101):
        cm()

profiler.print_stats(sort='cumtime')


# cProfile stats for: chocolate, caramel, single
#
# 117392 function calls in 0.141 seconds
#
#    Ordered by: cumulative time
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       100    0.009    0.000    0.111    0.001 research.py:13(init)
#      8500    0.046    0.000    0.051    0.000 research.py:24(create_candy_from_row)
#      8600    0.022    0.000    0.044    0.000 csv.py:107(__next__)
#       100    0.001    0.000    0.024    0.000 program.py:62(_get_matched_candy)
#       300    0.000    0.000    0.023    0.000 research.py:45(get_candy_by_descriptor)
#       300    0.004    0.000    0.023    0.000 research.py:48(<listcomp>)
#     13200    0.004    0.000    0.018    0.000 research.py:61(_convert_candy_to_dict)


# cProfile stats for: chocolate, caramel, single AFTER performance changes
#
# 31207 function calls in 0.025 seconds
#
#    Ordered by: cumulative time
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       100    0.000    0.000    0.018    0.000 program.py:62(_get_matched_candy)
#       300    0.000    0.000    0.018    0.000 research.py:56(get_candy_by_descriptor)
#       300    0.004    0.000    0.017    0.000 research.py:59(<listcomp>)
#     13200    0.003    0.000    0.014    0.000 research.py:72(_convert_candy_to_dict)
#     13200    0.010    0.000    0.010    0.000 __init__.py:423(_asdict)
#       700    0.005    0.000    0.006    0.000 {built-in method builtins.print}
#       792    0.001    0.000    0.001    0.000 __init__.py:419(__repr__)
#       100    0.000    0.000    0.001    0.000 research.py:12(init)
#        85    0.000    0.000    0.000    0.000 research.py:25(create_candy_from_row)
#        86    0.000    0.000    0.000    0.000 csv.py:107(__next__)
#       100    0.000    0.000    0.000    0.000 research.py:62(sort_matched_candy_by)
#       100    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
#        87    0.000    0.000    0.000    0.000 {built-in method builtins.next}
#       935    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
#       171    0.000    0.000    0.000    0.000 csv.py:93(fieldnames)
#       100    0.000    0.000    0.000    0.000 program.py:88(_check_second_input)
#        85    0.000    0.000    0.000    0.000 <string>:1(__new__)
#       100    0.000    0.000    0.000    0.000 research.py:66(get_top_five_candy)