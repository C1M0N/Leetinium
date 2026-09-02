"""
Course  : Leetinium 100
File    : 141_LinkedListCycle.py
Name    : Cimon

GitHub User: C1M0N
Date: 4/13/25 16:33
"""
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    >>> s = Solution()
    >>> s.hasCycle([3,2,0,-4])
    True

    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head
        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False


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