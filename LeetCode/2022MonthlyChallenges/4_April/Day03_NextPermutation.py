#Next Permutation
'''
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
    For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order,
then the next permutation of that array is the permutation that follows it in the sorted container.
If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

    For example, the next permutation of arr = [1,2,3] is [1,3,2].
    Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
    While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory.

Example:
    Input: nums = [1,2,3]
    Output: [1,3,2]
'''

class Solution:
    def nextPermutation(self,nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(L,start,end):
            while start<end:
                L[start],L[end]=L[end],L[start]
                start,end=start+1,end -1
        
        i,n=len(nums)-1,len(nums)
        while i>0 and nums[i]<=nums[i-1]:
            i-=1
        if i!=0:
            j=i
            while j+1<n and nums[j+1]>nums[i-1]:
                j+=1
            nums[i-1],nums[j]=nums[j],nums[i-1]
        reverse(nums,i,n-1)
        return nums