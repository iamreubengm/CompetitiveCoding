#Kth Missing Positive Number
'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Find the kth positive integer that is missing from this array.

Solution:
Create a set of the input array, and loop from 1 to k + length of the array as that
is all you need to traverse, and lookup each number in the set. If it is not in
the set, the k value is decremented. When k hits 0, we return the loop value i.
'''

class Solution:
    def findKthPositive(self,arr,k):
        arr_set=set(arr)
        for i in range(1,k+len(arr)+1):
            if i not in arr_set: 
                k-=1
            if k==0: 
                return i
    
