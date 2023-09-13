import math as m
# as m - alias
# from math import prod
from math import *
# * - import all methods

from my_module import sum_it

result = sum_it(4, 5)
print(result)


lst = [1, 2, 5, 7]
print(m.prod(lst))


def tests():
    assert sum_it(5, 8) == 13, f'Wrong number, actual result is {sum_it(5, 8)}'
    # assert sum_it(10, 10) == 28, f'Wrong number, actual result is {sum_it(10, 10)}'


tests()

import datetime
# from datetime import date

birth_year = 1984
current_date = datetime.date.today()
print(current_date)
current_age = current_date.year - birth_year
print(current_age)
