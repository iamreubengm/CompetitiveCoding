#Count Primes
'''
Count the number of prime numbers less than a non-negative number, n.

Example:
    Input: n = 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

class Solution:
    def countPrimes(self,n):
        s=[0,0]+[1]*(n-1)
        for i in range(int(n**0.5)+1):
            if s[i]:
                for j in range(i**2,n+1,i):
                    s[j]=0
        return sum(s[:-1])