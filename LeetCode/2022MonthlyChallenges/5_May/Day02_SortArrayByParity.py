#Sort Array By Parity
'''
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.

Example:
    Input: nums = [3,1,2,4]
    Output: [2,4,3,1]
    Explanation:
        The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
'''

class Solution:
    def sortArrayByParity(self,nums):
        l,r=0,len(nums)-1
        while l<=r:
            if not nums[l]%2:
                l+=1
            else:
                nums[l],nums[r]=nums[r],nums[l]
                r-=1
        return nums