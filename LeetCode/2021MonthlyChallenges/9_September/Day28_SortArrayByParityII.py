#Sort Array By Parity II
'''
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
Return any answer array that satisfies this condition.

Example:
    Input: nums = [4,2,5,7]
    Output: [4,5,2,7]
    Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
'''

class Solution:
    def sortArrayByParityII(self,nums):
        i,j=0,1
        n=len(nums)
        while i<n and j<n:
            if not nums[i]%2:
                i+=2
            elif nums[j]%2:
                j+=2
            else:
                nums[i],nums[j]=nums[j],nums[i]
        return nums