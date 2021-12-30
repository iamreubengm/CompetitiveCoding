#Smallest Integer Divisible by K
'''
Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.
Return the length of n. If there is no such n, return -1.
Note: n may not fit in a 64-bit signed integer.

Example:
    Input: k = 1
    Output: 1
    Explanation: The smallest answer is n = 1, which has length 1.
'''

class Solution:
    def smallestRepunitDivByK(self,k):
        if not k%2 or not k%5:
            return -1
        rem,res=1,1
        while rem%k:
            rem=(rem*10+1)%k
            res+=1
        return res