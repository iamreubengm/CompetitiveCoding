#Daily Temperatures
'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait
after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

    Example:
    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]
'''

from collections import deque
class Solution:
    def dailyTemperatures(self,temperatures):
        res,s=[0]*len(temperatures),deque()
        for i,x in enumerate(temperatures):
            while s and x>temperatures[s[-1]]:
                res[s[-1]]=i-s[-1]
                s.pop()
            s.append(i)
        return res