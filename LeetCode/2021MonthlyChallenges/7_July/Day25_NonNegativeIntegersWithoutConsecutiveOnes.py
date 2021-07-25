#Non-negative Integers without Consecutive Ones
'''
Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not contain consecutive ones.

Example:
    Input: n = 5
    Output: 5
    Explanation:
        Here are the non-negative integers <= 5 with their corresponding binary representations:
        0 : 0
        1 : 1
        2 : 10
        3 : 11
        4 : 100
        5 : 101
        Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule. 
'''

class Solution:
    def findIntegers(self,n):
        b=bin(n+1)[2:]
        l=len(b)
        d=[1,2]+[0]*(l-2)
        for i in range(2,l):
            d[i]=d[i-1]+d[i-2]
        f,res=0,0
        for i in range(l):
            if b[i]=='0':
                continue
            if f:
                break
            if i and b[i-1]=="1":
                f=1
            res+=d[-i-1]
        return res