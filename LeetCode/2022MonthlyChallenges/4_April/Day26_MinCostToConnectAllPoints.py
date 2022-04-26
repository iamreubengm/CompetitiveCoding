#Min Cost to Connect All Points
'''
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Example:
    Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    Output: 20
'''

class Solution:
    def minCostConnectPoints(self,points):
        res=0
        d={}
        for i,(x,y) in enumerate(points):
            if i:
                d[(x,y)]=float('inf')
            else:
                d[(x,y)]=0
        while d:
            x,y=min(d,key=d.get)
            res+=d.pop((x,y))
            for a,b in d:
                d[(a,b)]=min(d[(a,b)],abs(x-a)+abs(y-b))
        return res