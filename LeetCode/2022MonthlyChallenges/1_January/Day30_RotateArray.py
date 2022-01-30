#Rotate Array
'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example:
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
        rotate 1 steps to the right: [7,1,2,3,4,5,6]
        rotate 2 steps to the right: [6,7,1,2,3,4,5]
        rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''

class Solution:
    def rotate(self,nums,k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        start=0
        count=0
        while count<n:
            cur,prev=start,nums[start]
            while True:
                nindex=(cur+k)%n
                nums[nindex],prev=prev,nums[nindex]
                cur=nindex
                count+=1
                if start==cur:
                    break
            start+=1