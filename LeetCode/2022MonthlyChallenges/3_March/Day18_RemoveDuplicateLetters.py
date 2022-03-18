#Remove Duplicate Letters
'''
Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
    Input: s = "bcabc"
    Output: "abc"

    Input: s = "cbacdcbc"
    Output: "acdb"
'''

class Solution:
    def removeDuplicateLetters(self,s):
        last={x:i for i,x in enumerate(s)}
        stack=["."]
        for i,x in enumerate(s):
            if x not in stack:
                while (x<stack[-1] and last[stack[-1]]>i):
                    stack.pop()
                stack.append(x)
        return ''.join(stack[1:])