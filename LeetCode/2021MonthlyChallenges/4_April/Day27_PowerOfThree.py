#Power of Three
'''
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.

Follow up: Could you solve it without loops/recursion?

Example:
    Input: n = 27
    Output: true

Solution:
This can be solved in multiple ways. To meet the follow up condition, we use a mathematical
approach. A power of three can only be divided by other powers of three (3 is a Prime Number).
So we take the largest power of 3 in the range (3^19) and check if it is divisible by n.
'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return 0
        return (3**19)%n==0