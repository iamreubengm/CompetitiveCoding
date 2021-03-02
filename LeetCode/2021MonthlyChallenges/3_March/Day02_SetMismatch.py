#Set Mismatch
'''
You have a set of integers s, which originally contains all the numbers from 1 to n.
Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set,
which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example:
    Input: nums = [1,2,2,4]
    Output: [2,3]

Solution:
This can be solved in multiple ways. One solution is to use a separate list.
For each value in 'nums', that index in the new list 'l' is incremented by 1.
Thus, the missing value will not be incremented and will have value 0, while
the duplicate element will have value 2. Iterate through the list to find these
two values to get the result.
Another solution is to use simple math. The sum of the set of 'nums' subtracted
from the total sum of 'nums' gives the duplicate number. Similarly, the expected sum
of all numbers upto 'n' is performed using len(nums) * len(nums)+1 /2 and the sum of 
set of 'nums' is subtracted from it to get the missing number.
'''

class Solution:
    
    def findErrorNums1(self,nums):
        l=[0]*(len(nums)+1)
        for x in nums:
            l[x]+=1
        for x in range(len(l)):
            if l[x]==0:
                missing=x
            elif l[x]>1:
                duplicate=x
        return [duplicate,missing]
    
    def findErrorNums2(self,nums):
        duplicate=sum(nums)-sum(set(nums))
        missing=((len(nums)*(len(nums)+1))//2)-sum(set(nums))
        return[duplicate,missing]
