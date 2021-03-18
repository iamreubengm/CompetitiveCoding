#Wiggle Subsequence
'''
Given an integer array nums, return the length of the longest wiggle sequence.
A wiggle sequence is a sequence where the differences between successive numbers strictly alternate
between positive and negative. The first difference (if one exists) may be either positive or negative.
A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) are alternately positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences, the first because its first two differences are positive and
the second because its last difference is zero.
A subsequence is obtained by deleting some elements (eventually, also zero) from the original sequence,
leaving the remaining elements in their original order.

Solution:
We use inc and dec to store the sizes of the longest sequences. If we find the current element in the list is greater than
the previous element, we set the value of 'inc' to 'dec' plus 1.  We do the same for the other case. In the end, we return the 
greatest of 'inc' and 'dec'
'''

class Solution:
    def wiggleMaxLength(self,nums):
        if len(nums)<2:
            return len(nums)
        inc=1
        dec=1
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                dec=inc+1
            elif nums[i]>nums[i-1]:
                inc=dec+1
        return max(inc,dec)