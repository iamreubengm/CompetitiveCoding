#Critical Connections in a Network
'''
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where
connections[i] = [a, b] represents a connection between servers a and b.
Any server can reach any other server directly or indirectly through the network.
A critical connection is a connection that, if removed, will make some server unable to reach some other server.
Return all critical connections in the network in any order.

Example :
    Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
    Output: [[1,3]]
    Explanation: [[3,1]] is also accepted.
'''

class Solution:
    def criticalConnections(self,n,connections):
        edgeMap=defaultdict(list)
        for a,b in connections:
            edgeMap[a].append(b)
            edgeMap[b].append(a)
        disc,low,time,res=[0]*n,[0]*n,[1],[]
        
        def dfs(curr,prev):
            disc[curr]=low[curr]=time[0]
            time[0]+=1
            for next in edgeMap[curr]:
                if not disc[next]:
                    dfs(next,curr)
                    low[curr]=min(low[curr],low[next])
                elif next!=prev:
                    low[curr]=min(low[curr],disc[next])
                if low[next]>disc[curr]:
                    res.append([curr,next])
                    
        dfs(0,-1)
        return res