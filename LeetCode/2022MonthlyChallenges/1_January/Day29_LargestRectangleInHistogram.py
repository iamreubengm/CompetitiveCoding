#Largest Rectangle in Histogram
'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.

Example:
    Input: heights = [2,1,5,6,2,3]
    Output: 10
'''

class Solution:
    def largestRectangleArea(self,heights):
        s=[]
        res=0
        for i,x in enumerate(heights+[0]):
            while s and heights[s[-1]]>=x:
                h=heights[s.pop()]
                w=i if not s else i-1-s[-1]
                res=max(res,h*w)
            s.append(i)
        return res