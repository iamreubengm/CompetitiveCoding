#Partition Labels
'''
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
Return a list of integers representing the size of these parts.

Example:
    Input: s = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
        The partition is "ababcbaca", "defegde", "hijhklij".
        This is a partition so that each letter appears in at most one part.
        A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
'''

class Solution:
    def partitionLabels(self,s):
        res=[]
        last={}
        maxl,c=0,0
        for i,x in enumerate(s):
            last[x]=i
        for i,x in enumerate(s):
            maxl=max(maxl,last[x])
            c+=1
            if i==maxl:
                res.append(c)
                c=0
        return res