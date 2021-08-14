#Remove Boxes
'''
You are given several boxes with different colors represented by different positive numbers.
You may experience several rounds to remove boxes until there is no box left.
Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.
Return the maximum points you can get.

Example:
    Input: boxes = [1,3,2,2,2,3,4,3,1]
    Output: 23
    Explanation:
                [1, 3, 2, 2, 2, 3, 4, 3, 1] 
                ----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
                ----> [1, 3, 3, 3, 1] (1*1=1 points) 
                ----> [1, 1] (3*3=9 points) 
                ----> [] (2*2=4 points)
'''

from functools import lru_cache

class Solution:
    def removeBoxes(self,boxes):
        @lru_cache(None)
        def dp(l,r,k):
            if l>r:
                return 0
            while l+1<=r and boxes[l]==boxes[l + 1]:
                l+=1
                k+=1
            res=dp(l+1,r,0)+(k+1)*(k+1)
            for j in range(l+1,r+1):
                if boxes[l]==boxes[j]:
                    res=max(res,dp(j,r,k+1)+dp(l+1,j-1,0))
            return res
        return dp(0,len(boxes)-1,0)