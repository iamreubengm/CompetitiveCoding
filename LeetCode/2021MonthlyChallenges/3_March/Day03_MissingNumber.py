#Missing Number
'''
Given an array nums containing n distinct numbers in the range [0, n], return the
only number in the range that is missing from the array.
Follow up: Could you implement a solution using only O(1) extra space complexity
and O(n) runtime complexity?

Example:
    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
    2 is the missing number in the range since it does not appear in nums.
    
Solution:
This has a very simple Mathematical formula. We know that 'nums' contains all but 
one number in the range 0 to n, where n is the length of the list.
We can calculate the expected sum of the first n numbers using the formula: n*(n+1) / 2.
We can subtract the sum of all elements in 'nums' from this expected sum to get the 
missing number.
'''

class Solution:
    def missingNumber(self,nums):
        return (len(nums)*(len(nums)+1))//2 - sum(nums)
