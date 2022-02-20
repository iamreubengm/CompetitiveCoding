#Remove Covered Intervals
'''
Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.
The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.
Return the number of remaining intervals.

Example:
    Input: intervals = [[1,4],[3,6],[2,8]]
    Output: 2
    Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
'''

class Solution:
    def removeCoveredIntervals(self,intervals):
        res=0
        r=0
        intervals.sort(key=lambda x: (x[0],-x[1]))
        for i,j in intervals:
            if j>r:
                res+=1
            r=max(r,j)
        return res