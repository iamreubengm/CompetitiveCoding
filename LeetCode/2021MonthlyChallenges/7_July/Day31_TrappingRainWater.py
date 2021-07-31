#Trapping Rain Water
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
                In this case, 6 units of rain water (blue section) are being trapped.
'''

class Solution:
    def trap(self,height):
        if len(height)<3:
            return 0
        res=0
        l,r=0,len(height)-1
        lmax,rmax=height[l],height[r]
        while l<r:
            lmax=max(lmax,height[l])
            rmax=max(rmax,height[r])
            if lmax<=rmax:
                res+= lmax-height[l]
                l+=1
            else:
                res+=rmax-height[r]
                r-=1
        return res