#Contiguous Array
'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example:
    Input: nums = [0,1]
    Output: 2
    Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
'''

class Solution:
    def findMaxLength(self,nums):
        d={0:-1}
        c=0
        maxlen=0
        for i,x in enumerate(nums):
            if not x:
                c-=1
            else:
                c+=1
            if c in d:
                maxlen=max(maxlen,i-d[c])
            else:
                d[c]=i
        return maxlen