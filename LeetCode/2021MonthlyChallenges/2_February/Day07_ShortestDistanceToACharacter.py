#Shortest Distance to a Character
'''
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length
and answer[i] is the shortest distance from s[i] to the character c in s.

Example: Input: s = "loveleetcode", c = "e"
         Output: [3,2,1,0,1,0,0,1,2,2,1,0]
         
Solution:
This can be solved by doing two passes on the array.
The first pass finds the shortest distance to the character on the right.
The second backward pass finds the distance to the left.
Both passes have been merged into the for statement.
'''
class Solution:
    def shortestToChar(self,s,c):
        n=len(s)
        p=-float('inf')
        res=[n]*n
        for i in list(range(n)) + list(range(n)[::-1]):
            if s[i]==c:
                p=i
            res[i]=min(res[i],abs(i-p))
        return res