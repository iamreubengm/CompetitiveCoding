#Boats to Save People
'''
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit.
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.

Example:
    Input: people = [1,2], limit = 3
    Output: 1
    Explanation: 1 boat (1, 2)
'''

class Solution:
    def numRescueBoats(self,people,limit):
        res=0
        l,r=0,len(people)-1
        people.sort()
        while l<=r:
            if people[l]+people[r]<=limit:
                l+=1
            res+=1
            r-=1
        return res