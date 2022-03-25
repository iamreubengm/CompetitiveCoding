#Two City Scheduling
'''
A company is planning to interview 2n people.
Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

Example:
    Input: costs = [[10,20],[30,200],[400,50],[30,20]]
    Output: 110
    Explanation: 
        The first person goes to city A for a cost of 10.
        The second person goes to city A for a cost of 30.
        The third person goes to city B for a cost of 50.
        The fourth person goes to city B for a cost of 20.
        The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
'''

class Solution:
    def twoCitySchedCost(self,costs):
        costs.sort(key=lambda x: x[0]-x[1])
        a,b=0,0
        for x in costs[:len(costs)//2]:
            a+=x[0]
        for x in costs[len(costs)//2:]:
            b+=x[1]
        return a+b