#N-th Tribonacci Number
'''
The Tribonacci sequence Tn is defined as follows: 
    T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

Example:
    Input: n = 4
    Output: 4
    Explanation:
        T_3 = 0 + 1 + 1 = 2
        T_4 = 1 + 1 + 2 = 4
'''

class Solution:
    def tribonacci(self,n):
        a=[0,1,1]
        for i in range(3,n+1):
            a.append(a[i-1]+a[i-2]+a[i-3])
        return a[n]