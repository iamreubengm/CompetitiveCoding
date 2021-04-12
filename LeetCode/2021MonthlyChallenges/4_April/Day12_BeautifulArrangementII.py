#Beautiful Arrangement II
'''
Given two integers n and k, you need to construct a list which contains n different positive integers
ranging from 1 to n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|]
has exactly k distinct integers. If there are multiple answers, print any of them.

Example:
    Input: n = 3, k = 1
    Output: [1, 2, 3]
    Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1]
                 has exactly 1 distinct integer: 1.
'''

class Solution:
    def constructArray(self,n,k):
        res=list(range(1,n-k))
        for i in range(k+1):
            if i%2==0:
                res.append(n-k+i//2)
            else:
                res.append(n-i//2)
        return res