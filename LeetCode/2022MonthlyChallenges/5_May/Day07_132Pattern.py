#132 Pattern
'''
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
Return true if there is a 132 pattern in nums, otherwise, return false.

Example:
    Input: nums = [1,2,3,4]
    Output: false
    Explanation: There is no 132 pattern in the sequence.

    Input: nums = [3,1,4,2]
    Output: true
    Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
'''

class Solution:
    def find132pattern(self,nums):
        smallest=float('inf')
        stack=[]
        for i in nums:
            while stack and i>=stack[-1][-1]:
                stack.pop()
            if stack and i>stack[-1][0]:
                return True
            stack.append((smallest,i)) 
            smallest=min(smallest,i)
        return False