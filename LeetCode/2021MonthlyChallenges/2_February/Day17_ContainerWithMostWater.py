#Container With Most Water
'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
Notice that you may not slant the container.

Example:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
                 In this case, the max area of water (blue section) the container can contain is 49.

Solution:
We can solve this by having two pointers at either end of the heights list (l,r).
We take the minimum of the heights at both positions, and multiply them with the distance between them (r-l).
We replace this with the most_water variable if it is greater than the current value.
After that, we need to move the pointers, and we do that based on the heights at the current pointer values.
If the left pointer is smaller, the left pointer moves forward by 1, and in the other case, the right pointer
moves back by 1.
We finally return the most_water variable.
'''

class Solution:
    def maxArea(self,height):
        l=0
        r=len(height)-1
        most_water=0
        
        while l<r:
            most_water=max(most_water,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return most_water