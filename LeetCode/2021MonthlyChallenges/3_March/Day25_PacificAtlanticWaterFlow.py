#Pacific Atlantic Water Flow
'''
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent,
the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
    The order of returned grid coordinates does not matter.
    Both m and n are less than 150.
 
Example:

    Given the following 5x5 matrix:
      Pacific ~   ~   ~   ~   ~ 
           ~  1   2   2   3  (5) *
           ~  3   2   3  (4) (4) *
           ~  2   4  (5)  3   1  *
           ~ (6) (7)  1   4   5  *
           ~ (5)  1   1   2   4  *
              *   *   *   *   * Atlantic

    Return:
        [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
'''

class Solution:
    def pacificAtlantic(self,matrix):
        if not matrix or not matrix[0]:
            return []
        
        m,n=len(matrix[0]),len(matrix)
        
        def bfs(starts):
            queue=deque(starts)
            visited=set(starts)
            while queue:
                x,y=queue.popleft()
                for dx, dy in [(x, y+1),(x, y-1),(x-1, y),(x+1, y)]:
                    if 0<=dx<n and 0<=dy<m and (dx,dy) not in visited and matrix[dx][dy]>=matrix[x][y]:
                        queue.append((dx, dy))
                        visited.add((dx, dy))
            return visited
        
        pacific=[(0,i) for i in range(m)]+[(i,0) for i in range(1,n)]
        atlantic=[(n-1,i) for i in range(m)]+[(i, m-1) for i in range(n-1)]
        
        return bfs(pacific) & bfs(atlantic)