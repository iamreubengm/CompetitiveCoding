#Count of Smaller Numbers After Self
'''
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:
    Input: nums = [5,2,6,1]
    Output: [2,1,1,0]
    Explanation:
                To the right of 5 there are 2 smaller elements (2 and 1).
                To the right of 2 there is only 1 smaller element (1).
                To the right of 6 there is 1 smaller element (1).
                To the right of 1 there is 0 smaller element.
'''

from sortedcontainers import SortedList

class Solution:
    def countSmaller(self,nums):
        res=[0]*len(nums)
        sl=SortedList()
        for i,x in enumerate(nums[::-1]):
            index=SortedList.bisect_left(sl,x)
            res[i]=index
            sl.add(x)
        return res[::-1]