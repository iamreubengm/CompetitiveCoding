#Minimum Domino Rotations For Equal Row
'''
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino.
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.
Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.
If it cannot be done, return -1.

Example:
    Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
    Output: 2
    Explanation: 
        The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
        If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
'''

class Solution:
    def minDominoRotations(self,tops,bottoms):
        n=len(tops)
        ca=[0]*7
        cb=[0]*7
        same=[0]*7
        for i in range(n):
            a,b=tops[i],bottoms[i]
            ca[a]+=1
            cb[b]+=1
            if a==b:
                same[a]+=1
        res=n
        for i in range(1,7):
            if ca[i]+cb[i]-same[i]==n:
                res=min(res,min(ca[i],cb[i])-same[i])
        if res==n:
            return -1
        return res