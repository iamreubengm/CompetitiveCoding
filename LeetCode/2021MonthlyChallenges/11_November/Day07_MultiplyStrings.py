#Multiply Strings
'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
    Input: num1 = "2", num2 = "3"
    Output: "6"
'''

class Solution:
    def multiply(self,num1,num2):
        m,n=len(num1),len(num2)
        res=[0]*(m+n)
        for i,x in enumerate(num1[::-1]):
            for j,y in enumerate(num2[::-1]):
                res[i+j]+=int(x)*int(y)
                res[i+j+1]+=res[i+j]//10
                res[i+j]%=10
        while len(res)>1 and not res[-1]:
            res.pop()
        return ''.join(map(str,res[::-1]))