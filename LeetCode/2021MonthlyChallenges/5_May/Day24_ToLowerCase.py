#To Lower Case
'''
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Example:
    Input: s = "Hello"
    Output: "hello"
'''

class Solution:
    def toLowerCase(self,s):
        res=[]
        for x in s:
            if "A"<=x<="Z":
                res.append(chr(ord(x)+32))
            else:
                res.append(x)                
        return ''.join(res)