#Jump Game IV
'''
Given an array of integers arr, you are initially positioned at the first index of the array.
In one step you can jump from index i to index:
    i + 1 where: i + 1 < arr.length.
    i - 1 where: i - 1 >= 0.
    j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.
Notice that you can not jump outside of the array at any time.

Example:
    Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
    Output: 3
    Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
'''

from collections import defaultdict,deque

class Solution:
    def minJumps(self,arr):
        if len(arr) == 1:
            return 0

        adj=defaultdict(list)
        for i,x in enumerate(arr):
            adj[x].append(i)
        res=[0]*len(arr)
        dq=deque([len(arr)-1])
        while dq:
            i=dq.popleft()
            if i<len(arr)-1 and not res[i+1] and i+1<len(arr)-1:
                res[i+1]=res[i]+1
                dq.append(i+1)
            if i>0 and not res[i-1]:
                res[i-1]=res[i]+1
                if i-1==0:
                    return res[0]
                dq.append(i - 1)
            for j in adj[arr[i]]:
                if not res[j] and j<len(arr)-1:
                    res[j]=res[i]+1
                    if j==0:
                        return res[0]
                    dq.append(j)
            adj.pop(arr[i])
