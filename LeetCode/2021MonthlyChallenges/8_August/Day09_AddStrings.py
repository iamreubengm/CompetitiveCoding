#Add Strings
'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.

Example:
    Input: num1 = "11", num2 = "123"
    Output: "134"
'''

class Solution:
    def addStrings(self,num1,num2):
        num1,num2=list(num1),list(num2)
        c=0
        res=[]
        while len(num1) or len(num2):
            a,b=0,0
            if len(num1):
                a=ord(num1.pop())-ord('0')
            if len(num2):
                b=ord(num2.pop())-ord('0')
            t=a+b+c
            res.append(t%10)
            c=t//10
        if c:
            res.append(c)
        return ''.join(str(x) for x in res[::-1])