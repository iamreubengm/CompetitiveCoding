#Koko Eating Bananas
'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example:
Input: piles = [3,6,7,11], h = 8
Output: 4
'''

from math import ceil

class Solution:
    def minEatingSpeed(self,piles,h):
        l,r=0,max(piles)
        while l+1<r:
            m=(l+r)//2
            if sum(ceil(i/m) for i in piles)>h:
                l=m
            else:
                r=m
        return r