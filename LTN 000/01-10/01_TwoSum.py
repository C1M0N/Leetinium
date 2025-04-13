"""
Course  : Leetinium
File    : 01_TwoSum.py
Name    : Cimon

GitHub User: C1M0N
Date: 2025-04-13 16:13:38

"""
from typing import List


class Solution:
    """
    >>> s = Solution()

    >>> s.twoSum([2, 7, 11, 15], 9)
    [0, 1]
    >>> s.twoSum([3, 2, 4], 6)
    [1, 2]
    >>> s.twoSum([3, 3], 6)
    [0, 1]
    >>> s.twoSum([2,5,5,11], 10)
    [1, 2]
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]



def run_tests():
    import doctest

    doctest.testmod(verbose = True)


if __name__ == "__main__":
    run_tests()