#Merge Intervals
'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
'''

class Solution:
    def merge(self,intervals):
        intervals=sorted(intervals, key=lambda x:x[0])
        res=[]
        for x in intervals:
            if res and x[0]<=res[-1][1]:
                res[-1][1]=max(res[-1][1],x[1])
            else:
                res.append(x)
        return res