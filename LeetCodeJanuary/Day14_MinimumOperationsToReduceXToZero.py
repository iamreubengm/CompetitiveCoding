#Minimum Operations to Reduce X to Zero
'''
You are given an integer array nums and an integer x. In one operation,
you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. 
Note that this modifies the array for future operations.
Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.

Solution:
We use a sliding window to find the longest subarray that sums to the total sum
of nums minus the x value. The result is this length subtracted from the total
size of the array.
'''

class Solution:
    def minOperations(self,nums,x):
        t=sum(nums)-x
        size=-1
        window_sum=0
        l=-1
        n=len(nums)
        
        for h,num in enumerate(nums):
            window_sum+=num
            while l+1<n and window_sum>t:
                l+=1
                window_sum-=nums[l]
            if window_sum==t:
                size=max(size,h-l)
        if size<0:
            return -1
        else:
            return n-size