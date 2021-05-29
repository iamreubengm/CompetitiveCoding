#Maximum Erasure Value
'''
You are given an array of positive integers nums and want to erase a subarray containing unique elements.
The score you get by erasing the subarray is equal to the sum of its elements.
Return the maximum score you can get by erasing exactly one subarray.
An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

Example:
    Input: nums = [4,2,4,5,6]
    Output: 17
    Explanation: The optimal subarray here is [2,4,5,6].
'''

class Solution:
    def maximumUniqueSubarray(self,nums):
        visited=set()
        res,cur=0,0
        i=0
        for j in range(len(nums)):
            while nums[j] in visited:
                cur-=nums[i]
                visited.remove(nums[i])
                i+=1
            visited.add(nums[j])
            cur+=nums[j]
            res=max(cur,res)
        return res
                