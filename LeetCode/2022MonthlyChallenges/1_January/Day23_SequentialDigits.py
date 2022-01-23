#Sequential Digits
'''
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example:
    Input: low = 1000, high = 13000
    Output: [1234,2345,3456,4567,5678,6789,12345]
'''

from collections import deque

class Solution:
    def sequentialDigits(self,low,high):
        res=[]
        q=deque(range(1,10))
        while q:
            x=q.popleft()
            if low<=x<=high:
                res.append(x)
            l=x%10
            if l<9:
                q.append(x*10+l+1)
        return res