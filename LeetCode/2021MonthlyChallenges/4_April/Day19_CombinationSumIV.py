#Combination Sum IV
'''
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
The answer is guaranteed to fit in a 32-bit integer.

Example:
    Input: nums = [1,2,3], target = 4
    Output: 7
    Explanation: The possible combination ways are:
                 (1, 1, 1, 1)
                 (1, 1, 2)
                 (1, 2, 1)
                 (1, 3)
                 (2, 1, 1)
                 (2, 2)
                 (3, 1)
    Note that different sequences are counted as different combinations.
'''

class Solution:
    def combinationSum4(self,nums,target):
        dp=[0]*(target+1)
        for x in nums:
            if x<=target:
                dp[x]=1
        for i in range(target+1):
            for x in nums:
                if i-x>0:
                    dp[i]+=dp[i-x]
        return dp[-1]