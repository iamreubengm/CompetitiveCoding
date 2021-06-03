#Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
'''
Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts where horizontalCuts[i]
is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts.
Since the answer can be a huge number, return this modulo 10^9 + 7.

Example:
    Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
    Output: 4 
    Explanation: The figure above represents the given rectangular cake.
                 Red lines are the horizontal and vertical cuts.
                 After you cut the cake, the green piece of cake has the maximum area.
'''

class Solution:
    def maxArea(self,h,w,horizontalCuts,verticalCuts):
        hStrips=[0]+sorted(horizontalCuts)+[h]
        vStrips=[0]+sorted(verticalCuts)+[w]
        
        maxH,maxV=0,0
        for i in range(1,len(hStrips)):
            maxH=max(maxH,hStrips[i]-hStrips[i-1])
        for i in range(1,len(vStrips)):
            maxV=max(maxV,vStrips[i]-vStrips[i-1])
        
        return (maxH*maxV)%(10**9+7)