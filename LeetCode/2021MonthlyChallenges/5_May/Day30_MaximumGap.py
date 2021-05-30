#Maximum Gap
'''
Given an integer array nums, return the maximum difference between two successive elements in its sorted form.
If the array contains less than two elements, return 0.
You must write an algorithm that runs in linear time and uses linear extra space.

Example:
    Input: nums = [3,6,9,1]
    Output: 3
    Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
'''

class Solution:
    def maximumGap(self,nums):
        l,r,n=min(nums),max(nums),len(nums)
        if n<=2 or l==r:
            return r-l
        
        d={}
        for x in nums:
            if x==r:
                index=n-2
            else:
                index=(x-l)*(n-1)//(r-l)
            if index not in d:
                d[index]=[]
            d[index].append(x)

        r=[]
        for i in range(n-1):
            if i in d:
                r.append([min(d[i]),max(d[i])])
                
        maxdif=0
        for i in range(1,len(r)):
            dif=r[i][0]-r[i-1][1]
            if dif>maxdif:
                maxdif=dif
        return maxdif
        