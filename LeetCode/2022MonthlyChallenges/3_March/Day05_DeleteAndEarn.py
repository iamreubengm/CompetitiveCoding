#Delete and Earn
'''
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:
Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

Example:
    Input: nums = [3,4,2]
    Output: 6
    Explanation:
        You can perform the following operations:
        - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
        - Delete 2 to earn 2 points. nums = [].
        You earn a total of 6 points.
'''

class Solution:
    def deleteAndEarn(self,nums):
        d={}
        for x in nums:
            if x not in d:
                d[x]=0
            d[x]+=1
        k=sorted(d.keys())
        p,c=0,k[0]*d[k[0]]
        for i in range(1,len(k)):
            if k[i]-k[i-1]==1:
                p,c=c,max(c,p+k[i]*d[k[i]])
            else:
                p,c=c,c+k[i]*d[k[i]]
        return c