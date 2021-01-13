#Boats to Save People
'''
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.
Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.
(It is guaranteed each person can be carried by a boat.)

Example:
    Input: people = [3,2,2,1], limit = 3
    Output: 3
    Explanation: 3 boats (1, 2), (2) and (3)

Solution:
This uses a two pointer approach. Sort the list and then compare the heaviest and
lightest people. If their sum is less than or equal to the weight limit, the lower
pointer is moved forward. 
Since the boat can only accomodate two people, the number of boats is incremented 
and the high pointer is decremented after this check.
Finally the number of boats is returned.
'''

class Solution:
    def numRescueBoats(self,people,limit):
        num_boats=0
        l,h=0,len(people)-1
        people=sorted(people)
        while l<=h:
            if people[l]+people[h]<=limit:
                l+=1
            num_boats+=1
            h-=1
        return num_boats
                