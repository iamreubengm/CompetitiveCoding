#Sort Colors
'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example:
    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
'''

class Solution:
    def sortColors(self,nums):
        l,m,r=0,0,len(nums)-1
        while m<=r:
            if nums[m]==0:
                nums[l],nums[m]=nums[m],nums[l]
                m+=1
                l+=1
            elif nums[m]==2:
                nums[m],nums[r]=nums[r],nums[m]
                r-=1
            else:
                m+=1