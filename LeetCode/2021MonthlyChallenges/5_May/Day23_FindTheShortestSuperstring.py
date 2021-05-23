#Find the Shortest Superstring
'''
Given an array of strings words, return the smallest string that contains each string in words as a substring. If there are multiple valid strings of the smallest length, return any of them.
You may assume that no string in words is a substring of another string in words.

Example:
    Input: words = ["alex","loves","leetcode"]
    Output: "alexlovesleetcode"
    Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
'''

from itertools import permutations
class Solution:
    def CreateConnections(self,A,N):
        Connections=[[""]*N for _ in range(N)]
        for i, j in permutations(range(N),2):
            Connections[i][j]=A[j]
            for k in range(min(len(A[i]),len(A[j]))):
                if A[i][-k:]==A[j][:k]:
                    Connections[i][j]=A[j][k:]
        return Connections

    def shortestSuperstring(self,A):
        N=len(A)
        Connections=self.CreateConnections(A,N)
        dp=[[(float("inf"), "")]*N for _ in range(1<<N)]
        for i in range(N):
            dp[1<<i][i]=(len(A[i]),A[i])
            
        for mask in range(1<<N):
            n_z_bits=[j for j in range(N) if mask&(1<<j)]
            
            for j, k in permutations(n_z_bits,2):
                cand=dp[mask^(1<<j)][k][1]+Connections[k][j]
                dp[mask][j]=min(dp[mask][j],(len(cand),cand))

        return min(dp[-1])[1]   
        