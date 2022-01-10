#Add Binary
'''
Given two binary strings a and b, return their sum as a binary string.

Example:
    Input: a = "11", b = "1"
    Output: "100"
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i,j,s,carry = len(a)-1,len(b)-1,[],0
        while i>=0 or j>=0 or carry:
            d1=int(a[i]) if i >= 0 else 0
            d2=int(b[j]) if j >= 0 else 0
            s+=[str((d1+d2+carry)%2)]
            carry=(d1+d2+carry)//2
            i-=1
            j-=1
        return "".join(s[::-1])