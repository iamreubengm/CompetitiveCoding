#Minimum Remove to Make Valid Parentheses
'''
Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

Example:
    Input: s = "lee(t(c)o)de)"
    Output: "lee(t(c)o)de"
    Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
'''

class Solution:
    def minRemoveToMakeValid(self,s):
        s=list(s)
        stack=[]
        for i,x in enumerate(s):
            if x=='(':
                stack.append(i)
            elif x==')':
                if stack:
                    stack.pop()
                else:
                    s[i]=''
        while stack:
            s[stack.pop()]=''
        return ''.join(s)