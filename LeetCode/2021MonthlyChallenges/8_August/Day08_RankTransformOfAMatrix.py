#Rank Transform of a Matrix
'''
Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].
The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:
    The rank is an integer starting from 1.
    If two elements p and q are in the same row or column, then:
        If p < q then rank(p) < rank(q)
        If p == q then rank(p) == rank(q)
        If p > q then rank(p) > rank(q)
    The rank should be as small as possible.
It is guaranteed that answer is unique under the given rules.

Example:
    Input: matrix = [[1,2],[3,4]]
    Output: [[1,2],[2,3]]
    Explanation:
                The rank of matrix[0][0] is 1 because it is the smallest integer in its row and column.
                The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and matrix[0][0] is rank 1.
                The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and matrix[0][0] is rank 1.
                The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1] > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank 2.
'''

import collections

class Solution:
    def matrixRankTransform(self,matrix):
        n,m=len(matrix),len(matrix[0])
        rank=[0]*(m+n)
        d=collections.defaultdict(list)
        for i in range(n):
            for j in range(m):
                d[matrix[i][j]].append([i,j])
        
        def find(x):
            if p[x]!=x:
                p[x]=find(p[x])
            return p[x]
        
        for x in sorted(d):
            p=list(range(m+n))
            r=[i for i in rank]
            for i,j in d[x]:
                i,j=find(i),find(j+n)
                p[i]=j
                r[j]=max(r[i],r[j])
            for i,j in d[x]:
                rank[i]=rank[j+n]=matrix[i][j]=r[find(i)]+1
        return matrix