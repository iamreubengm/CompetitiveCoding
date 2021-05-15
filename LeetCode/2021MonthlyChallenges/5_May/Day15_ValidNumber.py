#Valid Number
'''
A valid number can be split up into these components (in order):
    A decimal number or an integer.
    (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):
    (Optional) A sign character (either '+' or '-').
    One of the following formats:
        At least one digit, followed by a dot '.'.
        At least one digit, followed by a dot '.', followed by at least one digit.
        A dot '.', followed by at least one digit.
An integer can be split up into these components (in order):
    (Optional) A sign character (either '+' or '-').
    At least one digit.

For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.
'''

class Solution:
    def isNumber(self,s):
        if not s:
            return False
        s=s.strip()
        decPointFlag,eFlag,digitFlag=0,0,0
        for i,x in enumerate(s):
            if x in ['+','-']:
                if i and s[i-1] not in ['E','e']:
                    return False
            elif x=='e' or x=='E':
                if eFlag or not digitFlag:
                    return False
                eFlag=1
                digitFlag=0
            elif x=='.':
                if decPointFlag or eFlag:
                    return False
                decPointFlag=1
            elif x.isdigit():
                digitFlag=1
            else:
                return False
        return digitFlag
        