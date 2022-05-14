#Network Delay Time
'''
You are given a network of n nodes, labeled from 1 to n.
You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example:
    Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
    Output: 2
'''

class Solution:
    def networkDelayTime(self,times,n,k):
        d=[float("inf") for i in range(n)]
        d[k-1] = 0
        for i in range(n-1):
            for u,v,w in times:
                if d[u-1]+w<d[v-1]:
                    d[v-1]=d[u-1]+w
        if max(d)<float("inf"):
            return max(d)
        return -1