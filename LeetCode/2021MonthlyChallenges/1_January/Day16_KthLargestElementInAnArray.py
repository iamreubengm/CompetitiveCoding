#Kth Largest Element in an Array
'''
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example:
    Input: [3,2,1,5,6,4] and k = 2
    Output: 5
    
Solution:
The quickest and easiest solution is sorting the list and returning the '-k-th element.
A more detailed method is Quick Select.
First we randomly choose a pivot element from nums.
Then we partition nums into 3 lists, based on if they are greater than, equal to or less than the pivot.
Then we compare k with the lengths of the lists. 
If it is less than the length of the lower list, the operation is again performed on the left list.
If k is greater than the lengths of less than and equal to lists, the operation is performed on the right list
with the appropriate modified k value
And if both the above conditions do not hold, you return mid[0] as all elements here are equal.
'''
import random

class Solution:
    def findKthLargestSimple(self,nums,k):
        s=sorted(nums)
        return s[-k]
    
    def findKthLargest(self,nums,k):
        pivot=random.choice(nums)
        left=[x for x in nums if x>pivot]
        mid =[x for x in nums if x==pivot]
        right=[x for x in nums if x<pivot]
        
        L,M=len(left),len(mid)
        if k<=L:
            return self.findKthLargest(left,k)
        elif k>L+M:
            return self.findKthLargest(right,k-L-M)
        else:
            return mid[0]