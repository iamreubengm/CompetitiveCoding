#Check If All 1's Are at Least Length K Places Away
'''
Given an array nums of 0s and 1s and an integer k, return True if all 1's 
are at least k places away from each other, otherwise return False.

Example: Input: nums = [1,0,0,0,1,0,0,1], k = 2
        Output: true
        Explanation: Each of the 1s are at least 2 places away from each other.
        
Solution:
This problem requires you to iterate through the list, and maintain a counter
of the number of zeros encountered. If it encounters a 1, and if the zero counter
is atleast k, it resets the counter and continues. If the counter value is less than
k, it returns false.
If it continues till the end, true is returned.
'''

class Solution:
    def kLengthApart(self,nums,k):
        c=k
        
        for i in nums:
            if i==0:
                c+=1
            elif i==1 and c>=k:
                c=0
            else:
                return False
        return True