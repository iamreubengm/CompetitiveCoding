#Sort Characters By Frequency
'''
Given a string s, sort it in decreasing order based on the frequency of the characters.
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

Example:
    Input: s = "tree"
    Output: "eert"
    Explanation:
        'e' appears twice while 'r' and 't' both appear once.
        So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
'''

class Solution:
    def frequencySort(self,s):
        d={}
        res=''
        for x in s:
            if x not in d:
                d[x]=0
            d[x]+=1
        d=sorted(d.items(), key=lambda x:x[1],reverse=True)
        for i,x in enumerate(d):
            res+=''.join(x[0]*x[1])
        return res