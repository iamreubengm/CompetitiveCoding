#Number of 1 Bits
'''
Write a function that takes an unsigned integer and returns the number of '1' bits it has
(also known as the Hamming weight).

Example: Input: n = 00000000000000000000000000001011
         Output: 3
         Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
         
Solution:
This can be completed in multiple ways but an efficient method is to use a bit manipulation trick.
For a number 'n', n&n-1 removes the rightmost bit so we count the number of times this operation
till the number becomes 0 to get the number of 1 bits.
'''

class Solution:
    def hammingWeight(self,n):
        count=0
        while n:
            n=n&(n-1)
            count+=1
        return count