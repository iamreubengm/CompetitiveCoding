#Find the Most Competitive Subsequence
'''
Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.
An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.
We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position
where a and b differ, subsequence a has a number less than the corresponding number in b. 
For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

Example:
    Input: nums = [3,5,2,6], k = 2
    Output: [2,6]
    Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]},
    [2,6] is the most competitive.
    
Solution:
This can be visualised as a stack problem, where nums is traversed from Left to Right.
If the encountered element is less than the last element in the stack, it is added on
after the last element is popped. This is done until you have len(nums)-k attempts.
Once that is done, the stack is returned upto k elements.
'''

class Solution:
    def mostCompetitive(self,nums,k):
        s=[]
        att=len(nums)-k
        for i in nums:
            while s and att and i<s[-1]:
                s.pop()
                att-=1
            s.append(i)
        return s[:k]
