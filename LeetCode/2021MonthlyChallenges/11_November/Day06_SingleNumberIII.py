#Single Number III
'''
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
Find the two elements that appear only once. You can return the answer in any order.
You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example:
    Input: nums = [1,2,1,3,2,5]
    Output: [3,5]
    Explanation:  [5, 3] is also a valid answer.
'''

class Solution:
    def singleNumber(self,nums):
        s=set()
        for x in nums:
            if x in s:
                s.remove(x)
            else:
                s.add(x)
        return s
    
    def singleNumber2(self,nums):
        x1,x2,i=0,0,0
        for x in nums:
            x1^=x
        for b in range(32):
            if x1&1<<b:
                i=b
                break
        for x in nums:
            if x&1<<i:
                x2^=x
        return [x1^x2,x2]