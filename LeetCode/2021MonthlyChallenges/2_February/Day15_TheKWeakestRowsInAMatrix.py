#The K Weakest Rows in a Matrix
'''
Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes
of the k weakest rows in the matrix ordered from the weakest to the strongest.
A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j,
or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row,
that is, always ones may appear first and then zeros.

Example:
Input: mat = 
            [[1,1,0,0,0],
             [1,1,1,1,0],
             [1,0,0,0,0],
             [1,1,0,0,0],
             [1,1,1,1,1]], 
            k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 2 
row 1 -> 4 
row 2 -> 1 
row 3 -> 2 
row 4 -> 5 
Rows ordered from the weakest to the strongest are [2,0,3,1,4]

Solution:
This can be solved by using a dictionary. Traverse the matrix and store the number of 1's
in each entry of the dictionary. It is then sorted based on it's values and the first 'k'
values are returned.
'''

class Solution:
    def kWeakestRows(self,mat,k):
        d={}
        for i,row in enumerate(mat):
            d[i]=0
            for n in row:
                if n:
                    d[i]+=1
                else:
                    break
        res=sorted(d,key=d.get)
        return res[:k]