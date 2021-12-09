#Jump Game III
'''
Given an array of non-negative integers arr, you are initially positioned at start index of the array.
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.
Notice that you can not jump outside of the array at any time.

Example:
    Input: arr = [4,2,3,0,3,1,2], start = 5
    Output: true
    Explanation: 
        All possible ways to reach at index 3 with value 0 are: 
        index 5 -> index 4 -> index 1 -> index 3 
        index 5 -> index 6 -> index 4 -> index 1 -> index 3 
'''

class Solution:
    def canReach(self,arr,start):
        if start<0 or start>=len(arr) or arr[start]<0:
            return False
        arr[start]*=-1
        return arr[start]==0 or self.canReach(arr,start+arr[start]) or self.canReach(arr,start-arr[start])