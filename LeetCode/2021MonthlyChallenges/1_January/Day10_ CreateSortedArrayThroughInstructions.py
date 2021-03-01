#Create Sorted Array through Instructions
'''
Given an integer array instructions, you are asked to create a sorted array from the elements in instructions. 
You start with an empty container nums. For each element from left to right in instructions, insert it into nums. 
The cost of each insertion is the minimum of the following:

    The number of elements currently in nums that are strictly less than instructions[i].
    The number of elements currently in nums that are strictly greater than instructions[i].
    For example, if inserting element 3 into nums = [1,2,3,5], 
        the cost of insertion is min(2, 1) (elements 1 and 2 are less than 3, element 5 is greater than 3) and nums will become [1,2,3,3,5].

Return the total cost to insert all elements from instructions into nums. 
Since the answer may be large, return it modulo 109 + 7

Solution:
A simple solution is to use a SortedList and use bisect functions to insert
the numbers in the left and right indexes, and choose the min among them.
To get number of elements strictly greater than current element, 
you use len(l)-bisect_right(i).
Answer is returned after the modulo operation.
'''

from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self,instructions):
        l=SortedList()
        res=0
        for i in instructions:
            res+=min(l.bisect_left(i),len(l)-l.bisect_right(i))
            l.add(i)
        return res%(10**9+7)
            