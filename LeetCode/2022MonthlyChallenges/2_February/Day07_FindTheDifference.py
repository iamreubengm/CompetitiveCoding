#Find the Difference
'''
You are given two strings s and t.
String t is generated by random shuffling string s and then add one more letter at a random position.
Return the letter that was added to t.

Example:
    Input: s = "abcd", t = "abcde"
    Output: "e"
    Explanation: 'e' is the letter that was added.
'''

class Solution:
    def findTheDifference(self,s,t):
        d={}
        for x in s:
            if x not in d:
                d[x]=0
            d[x]+=1
        for x in t:
            if x not in d or not d[x]:
                return x
            d[x]-=1