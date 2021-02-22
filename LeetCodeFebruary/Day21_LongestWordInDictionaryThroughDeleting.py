#Longest Word in Dictionary through Deleting
'''
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by
deleting some characters of the given string.
If there are more than one possible results, return the longest word with the smallest lexicographical order.
If there is no possible result, return the empty string.

Example:
    Input: s = "abpcplea", d = ["ale","apple","monkey","plea"]
    Output: "apple"

Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
'''

class Solution:
    def isSubsequence(self,s,t):
        i,j=0,0
        while i<len(s) and j<len(t):
            i,j=i+(s[i]==t[j]),j+1
        return i==len(s)
    
    def findLongestWord(self, s, d):
        res=""
        for string in d:
            if self.isSubsequence(string, s):
                res=min(res,string,key=lambda x:(-len(x), x))
        return res
