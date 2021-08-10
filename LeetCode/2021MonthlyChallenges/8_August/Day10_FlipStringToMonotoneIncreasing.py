#Flip String to Monotone Increasing
'''
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).
You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
Return the minimum number of flips to make s monotone increasing.

Example:
    Input: s = "00110"
    Output: 1
    Explanation: We flip the last digit to get 00111.
'''

class Solution:
    def minFlipsMonoIncr(self,s):
        zero_flip=s.count('0')
        one_flip=0
        res=len(s)-zero_flip
        for x in s:
            if x=='0':
                zero_flip-=1
            else:
                res=min(res,zero_flip+one_flip)
                one_flip+=1
        return res