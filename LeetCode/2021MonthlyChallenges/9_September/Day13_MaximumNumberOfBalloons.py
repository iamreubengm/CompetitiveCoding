#Maximum Number of Balloons
'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example:
    Input: text = "leetcode"
    Output: 0

    Input: text = "loonbalxballpoon"
    Output: 2
'''

class Solution:
    def maxNumberOfBalloons(self,text):
        c={}
        for x in text:
            if x not in c:
                c[x]=0
            c[x]+=1
        return min(c.get('b',0),c.get('a',0),c.get('l',0)//2,c.get('o',0)//2,c.get('n',0))