#Kth Smallest Number in Multiplication Table
'''
Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).
Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.

Example:
    Input: m = 3, n = 3, k = 5
    Output: 3
    Explanation: The 5th smallest number is 3.
'''

class Solution:
    def findKthNumber(self,m,n,k):
        def check(x):
            res=0
            for i in range(1,m+1):
                res+=min(n,x//i)
            return res>=k
        
        l,r=1,m*n
        while l<r:
            mid=(l+r)//2
            if not check(mid):
                l=mid+1
            else:
                r=mid
        return l