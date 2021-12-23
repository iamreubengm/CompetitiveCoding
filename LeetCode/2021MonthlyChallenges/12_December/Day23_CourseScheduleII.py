#Course Schedule II
'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them.
If it is impossible to finish all courses, return an empty array.

Example:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: [0,1]
    Explanation:
        There are a total of 2 courses to take.
        To take course 1 you should have finished course 0. So the correct course order is [0,1].
'''

from collections import defaultdict

class Solution:
    def findOrder(self,numCourses,prerequisites):
        def dfs(x):
            res.append(x)
            ind[x]=-1
            for course in graph[x]:
                ind[course]-=1
                if not ind[course]:
                    dfs(course)
        
        graph=defaultdict(list)
        ind=[0]*numCourses
        res=[]
        for c2,c1 in prerequisites:
            graph[c1].append(c2)
            ind[c2]+=1
        for i in range(numCourses):
            if not ind[i]:
                dfs(i)
        if len(res)==numCourses:
            return res
        return []