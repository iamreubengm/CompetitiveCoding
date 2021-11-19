#Hamming Distance
'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.

Example 1:
    Input: x = 1, y = 4
    Output: 2
    Explanation:
        1   (0 0 0 1)
        4   (0 1 0 0)
            ↑   ↑
        The above arrows point to positions where the corresponding bits are different.
'''

class Solution:
    def hammingDistance(self,x,y):
        xor=x^y
        res=0
        for i in range(32):
            res+=xor&(1<<i)!=0
        return res