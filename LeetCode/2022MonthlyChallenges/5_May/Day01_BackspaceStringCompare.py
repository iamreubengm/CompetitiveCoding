#Backspace String Compare
'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example:
    Input: s = "ab#c", t = "ad#c"
    Output: true
    Explanation: Both s and t become "ac".
'''

class Solution:
    def backspaceCompare(self,s,t):
        def check(string):
            t=[]
            for x in string:
                if x!='#':
                    t.append(x)
                elif x=='#' and len(t)>0:
                    t.pop()
            return t
        return check(s)==check(t)