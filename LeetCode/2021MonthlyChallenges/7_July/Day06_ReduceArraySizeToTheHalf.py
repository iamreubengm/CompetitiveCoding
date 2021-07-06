#Reduce Array Size to The Half
'''
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.
Return the minimum size of the set so that at least half of the integers of the array are removed.

Example:
    Input: arr = [3,3,3,3,5,5,5,2,2,7]
    Output: 2
    Explanation:
        Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
        Possible sets of size 2 are {3,5},{3,2},{5,2}.
        Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.
'''

class Solution:
    def minSetSize(self,arr):
        d={}
        for x in arr:
            if x  not in d:
                d[x]=0
            d[x]+=1
        f=sorted(list(d.values()))
        res,rem=0,0
        h=len(arr)//2
        while rem<h:
            res+=1
            rem+=f.pop()
        return res