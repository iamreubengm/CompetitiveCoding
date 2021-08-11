#Array of Doubled Pairs
'''
Given an array of integers arr of even length, return true if and only if it is possible to reorder it
such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2.

Example:
    Input: arr = [4,-2,2,-4]
    Output: true
    Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
'''

import collections

class Solution:
    def canReorderDoubled(self, arr):
        d=collections.Counter(arr)
        for x in sorted(d,key=abs):
            if d[x]>d[2*x]:
                return False
            d[2*x]-=d[x]
        return True