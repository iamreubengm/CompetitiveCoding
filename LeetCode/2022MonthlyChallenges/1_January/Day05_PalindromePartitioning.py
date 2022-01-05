#Palindrome Partitioning
'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
A palindrome string is a string that reads the same backward as forward.

Example:
    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]
'''

class Solution:
    def partition(self,s):
        def dfs(s,path,res):
            if not s:
                res.append(path[:])
                return
            for i in range(1,len(s)+1):
                if s[:i]==s[i-1::-1]:
                    path.append(s[:i])
                    dfs(s[i:],path,res)
                    path.pop()
        res=[]
        dfs(s,[],res)
        return res