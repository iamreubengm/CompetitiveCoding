#Global and Local Inversions
'''
We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.
The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].
The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].
Return true if and only if the number of global inversions is equal to the number of local inversions.

Example:
    Input: A = [1,0,2]
    Output: true
    Explanation: There is 1 global inversion, and 1 local inversion.
    
    Input: A = [1,2,0]
    Output: false
    Explanation: There are 2 global inversions, and 1 local inversion.
'''

class Solution:
    def isIdealPermutation(self,A):
        cmax=0
        for i in range(len(A)-2):
            cmax=max(cmax,A[i])
            if cmax>A[i+2]:
                return False
        return True
