#Reordered Power of 2
'''
Starting with a positive integer N, we reorder the digits in any order (including the original order)
such that the leading digit is not zero.
Return true if and only if we can do this in a way such that the resulting number is a power of 2.

Example:
    Input: 1
    Output: true
    
    Input: 10
    Output: false
    
    Input: 16
    Output: true
'''

from collections import Counter
class Solution:
    def reorderedPowerOf2(self,N):
        counter=Counter(str(N))
        return any(counter==Counter(str(1<<i))for i in range(30))