#Word Subsets
'''
We are given two arrays A and B of words.  Each word is a string of lowercase letters.
Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity. 
For example, "wrr" is a subset of "warrior", but is not a subset of "world".
Now say a word a from A is universal if for every b in B, b is a subset of a. 
Return a list of all universal words in A.  You can return the words in any order.

Example:
    Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
    Output: ["facebook","google","leetcode"]

Solution:
We first create a dictionary that stores the maximum occurances of each letter in each word in 'B'.
After that we go through each word in A, and ensure it has atleast d[x] occurances of x in it.
If it doesn't, we change the flag 'f' to 0 and break out. Only if the flag is not altered do we add
the word to the result. Finally we return the result.
'''

class Solution:
    def wordSubsets(self,A,B):
        d={}
        for b in B:
            for x in b:
                d[x]=max(b.count(x),d.get(x,0))
        res=[]
        for a in A:
            f=1
            for x in d.keys():
                if a.count(x)<d[x]:
                    f=0
                    break
            if f:
                res.append(a)
        return res  