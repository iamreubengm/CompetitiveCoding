#Brick Wall
'''
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks.
The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.
The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.
If your line go through the edge of a brick, then the brick is not considered as crossed.
You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.
You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Example:
    Input: [[1,2,2,1],
            [3,1,2],
            [1,3,2],
            [2,4],
            [3,1,2],
            [1,3,1,1]]
    Output: 2
    
Solution:
We use a dictionary to store the distances from the start of the wall where a brick has it's end point. We ignore the last brick at every level
as it goes upto the end which is not counted. We then return the point which has the maximum endpoints subtracted from the total length of the wall.
If there is only one brick per level of the same size, we simply return the length of the wall.
'''

class Solution:
    def leastBricks(self,wall):
        d={}
        for x in wall:
            i=0
            for y in x[:-1]:
                i+=y
                if i not in d:
                    d[i]=0
                d[i]+=1
        if d.values():
            return len(wall)-max(d.values())
        return len(wall)



