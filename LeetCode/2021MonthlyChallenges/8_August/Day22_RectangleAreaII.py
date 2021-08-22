#Rectangle Area II
'''
We are given a list of (axis-aligned) rectangles. Each rectangle[i] = [xi1, yi1, xi2, yi2] , where (xi1, yi1) are the coordinates of the bottom-left corner,
and (xi2, yi2) are the coordinates of the top-right corner of the ith rectangle.
Find the total area covered by all rectangles in the plane. Since the answer may be too large, return it modulo 109 + 7.

Example:
    Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
    Output: 6
'''

class Solution:
    def rectangleArea(self,rectangles):
        xs=sorted(set([x for x1,y1,x2,y2 in rectangles for x in [x1,x2]]))
        ys=sorted(set([y for x1,y1,x2,y2 in rectangles for y in [y1,y2]]))
        x_i={v: i for i,v in enumerate(xs)}
        y_i={v: i for i,v in enumerate(ys)}
        m,n=len(y_i),len(x_i)
        
        grid=[[0]*m for i in range(n)]
        for x1, y1, x2, y2 in rectangles:
            for x in range(x_i[x1], x_i[x2]):
                for y in range(y_i[y1], y_i[y2]):
                    grid[x][y]=1
        res=0
        for x in range(n-1):
            for y in range(m-1):
                res+=grid[x][y]*(xs[x+1]-xs[x])*(ys[y+1]-ys[y])
        return res%(10**9+7)