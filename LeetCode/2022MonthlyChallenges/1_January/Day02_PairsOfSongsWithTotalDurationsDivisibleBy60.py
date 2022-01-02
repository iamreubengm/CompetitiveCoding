#Pairs of Songs With Total Durations Divisible by 60
'''
You are given a list of songs where the ith song has a duration of time[i] seconds.
Return the number of pairs of songs for which their total duration in seconds is divisible by 60.
Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

Example:
    Input: time = [30,20,150,100,40]
    Output: 3
    Explanation:
        Three pairs have a total duration divisible by 60:
        (time[0] = 30, time[2] = 150): total duration 180
        (time[1] = 20, time[3] = 100): total duration 120
        (time[1] = 20, time[4] = 40): total duration 60
'''

class Solution:
    def numPairsDivisibleBy60(self,time):
        res=0
        count=[0]*60
        for t in time:
            x=t%60
            if x:
                res+=count[60-x]
            else:
                res+=count[0]
            count[x]+=1
        return res