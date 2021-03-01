#Distribute Candies
'''
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she
started to gain weight, so she visited a doctor.
The doctor advised Alice to only eat n / 2 of the candies she has (n is always even).
Alice likes her candies very much, and she wants to eat the maximum number of different
types of candies while still following the doctor's advice.
Given the integer array candyType of length n, return the maximum number of different types
of candies she can eat if she only eats n / 2 of them.

Example:
    Input: candyType = [6,6,6,6]
    Output: 1
    Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies,
                 she only has 1 type.
    
Solution:
The maximum number of candy types Alice can have is the minimum value between the 
total types of candies and n/2 (n is the total number of candies).
To get the number of types of candies, we create a dictionary that stores the unique
candy types. We then return the minimum value between n/2 and len(d.keys()).
'''

class Solution:
    def distributeCandies(self,candyType):
        d={}
        for x in candyType:
            if x not in d:
                d[x]=1
        return min(len(d.keys()),len(candyType)//2)
    
