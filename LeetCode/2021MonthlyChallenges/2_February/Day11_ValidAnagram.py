#Valid Anagram
'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example: Input: s = "anagram", t = "nagaram"
         Output: true
         
Solution:
This is a simple problem that can be solved a number of ways.
The simplest approach is to sort the strings and check if they are equal.
Another way is to use a hashmap, to store the occurances of each character in s.
Then go through 't' and check if the elements are in the hashmap. If not, they aren't anagrams.
If the character exists, decrement it's count. Finally check if all the counts are 0, which show
they are anagrams.
'''

class Solution:
    def isAnagram1(self, s, t):
        return sorted(s) == sorted(t)
    
    def isAnagram2(self,s,t):
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in t:
            if i not in d:
                return False
            else:
                d[i]-=1
        for i in d.values():
            if i!=0:
                return False
        return True

