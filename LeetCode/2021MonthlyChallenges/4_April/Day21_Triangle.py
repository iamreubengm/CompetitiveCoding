#Triangle
'''
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below.
More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example:
    Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    Output: 11
    Explanation: The triangle looks like:
                   #2
                  #3 4
                 6 #5 7
                4 #1 8 3
                The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (# above).
'''

class Solution:
    def minimumTotal(self,triangle):
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                if j==0:
                    triangle[i][j]+=triangle[i-1][j]
                elif j==len(triangle[i])-1:
                    triangle[i][j]+=triangle[i-1][j-1]
                else:
                    triangle[i][j]+=min(triangle[i-1][j-1],triangle[i-1][j])
        return min(triangle[-1])
