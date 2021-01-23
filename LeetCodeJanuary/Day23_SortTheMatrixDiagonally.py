#Sort the Matrix Diagonally
'''
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or
leftmost column and going in the bottom-right direction until reaching the matrix's end.
For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix,
includes cells mat[2][0], mat[3][1], and mat[4][2].
Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and
return the resulting matrix.

Example:
    Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
    Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
    
    3 3 1 1                  1 1 1 1
    2 2 1 2        ->        1 2 2 2
    1 1 1 2                  1 2 3 3

Solution:
The elements of a diagonal have the index [j-i] while traversing the matrix. In a 
dictionary, store the values of each diagonal in a list. Then sort that list in
descending order as when we are recreating the array, the largest element would
be at the bottom of the diagonal. Once sorted, traverse the matrix and assign the 
diagonal elements by popping from the dctionary's coresponding entry.
'''

from collections import defaultdict
class Solution:
    def diagonalSort(self,mat):
        m,n=len(mat),len(mat[0])
        d=defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[j-i].append(mat[i][j])
        for i in d:
            d[i].sort(reverse=True)
        
        for i in range(m):
            for j in range(n):
                mat[i][j]=d[j-i].pop()
        return mat
