#Next Permutation
'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.

Example:
    Input: nums = [1,2,3]
    Output: [1,3,2]
'''

class Solution:
    def nextPermutation(self,nums):
        def reverse(L,start,end):
            while start<end:
                L[start],L[end]=L[end],L[start]
                start,end=start+1,end -1
        
        i,n=len(nums)-1,len(nums)
        while i>=1 and nums[i]<=nums[i-1]:
            i-=1
            
        if i!=0:
            j=i
            while j+1<n and nums[j+1]>nums[i-1]:
                j+=1
            
            nums[i-1],nums[j]=nums[j],nums[i-1]
        
        reverse(nums,i,n-1)
        
        return nums
        