"""
Course  : Leetinium
File    : 33333.py
Name    : Cimon

GitHub User: C1M0N
Date: 4/21/25 17:10
"""
from functools import reduce


def get_all_sum(lst):
    '''
       >>> get_all_sum([5, -1, 12, -10, 2, 8])
       38
    '''
    new_lst = [abs(num) for num in lst]
    return reduce(lambda a,b: a+ b,new_lst)

numList = [2, -1, 4, 16]
print ([num * 2 for num in numList])

# region dev
def run_tests():
    import doctest

    doctest.testmod(verbose = True)


def main():
    run_tests()

    pass


if __name__ == "__main__":
    main()
# endregion
