#Maximum Performance of a Team
'''
You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n.
speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.
Choose at most k different engineers out of the n engineers to form a team with the maximum performance.
The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.
Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.

Example:
    Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
    Output: 60
    Explanation: 
                We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7).
                That is, performance = (10 + 5) * min(4, 7) = 60.
'''
import heapq
class Solution:
    def maxPerformance(self,n,speed,efficiency,k):
        h=[]
        res,speedSum=0,0
        d=sorted(zip(efficiency,speed),reverse=1)
        for e,s in d:
            heapq.heappush(h,s)
            speedSum+=s
            if len(h)>k:
                speedSum-=heapq.heappop(h)
            res=max(res,speedSum*e)
        return res%(10**9+7)