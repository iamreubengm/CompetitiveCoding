#Generate Random Point in a Circle
'''
Given the radius and x-y positions of the center of a circle, write a function randPoint
which generates a uniform random point in the circle.

Note:
    input and output values are in floating-point.
    radius and x-y position of the center of the circle is passed into the class constructor.
    a point on the circumference of the circle is considered to be in the circle.
    randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.
    
Example:
    Input: ["Solution","randPoint","randPoint","randPoint"]
           [[1,0,0],[],[],[]]
    Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]
'''

class Solution:

    def __init__(self,radius,x_center,y_center):
        self.r=radius
        self.x=x_center
        self.y=y_center
        

    def randPoint(self):
        t=uniform(0,2*pi)
        R=self.r*sqrt(uniform(0,1))
        return [self.x+R*cos(t),self.y+R*sin(t)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()