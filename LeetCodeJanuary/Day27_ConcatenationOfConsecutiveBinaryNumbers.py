#Concatenation of Consecutive Binary Numbers
'''
Given an integer n, return the decimal value of the binary string formed by concatenating
the binary representations of 1 to n in order, modulo 109 + 7.
Example: Input: n = 3
        Output: 27
        Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
        After concatenating them, we have "11011", which corresponds to the decimal value 27.

Solution:
A simple solution would be to create a string by iterating through all numbers upto n,
adding its binary equivalent and then returning the solution after dividing by 10^9+7
Another solution is obtained by observing the pattern based on n:
    1
    110 =1*100+10
    11011 = 110*100+11
    11011100 = 11011*1000+100
We can see that on each step we need to multiply number by length of new number and add new number(and use %M).

'''

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans=0
        for x in range(n):
            ans=(ans*(1<<(len(bin(x+1))-2))+x+1)%(10**9 + 7)
        return ans