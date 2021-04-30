#Powerful Integers
'''
Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.
An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.
You may return the answer in any order. In your answer, each value should occur at most once.

Example:
    Input: x = 2, y = 3, bound = 10
    Output: [2,3,4,5,7,9,10]
    Explanation:
                2 = 2^0 + 3^0
                3 = 2^1 + 3^0
                4 = 2^0 + 3^1
                5 = 2^1 + 3^1
                7 = 2^2 + 3^1
                9 = 2^3 + 3^0
                10 = 2^0 + 3^2
'''

class Solution:
    def powerfulIntegers(self,x,y,bound):
        px,py=[1],[1]
        if x>1:
            while px[-1]*x<bound:
                px.append(px[-1]*x)
        if y>1:
            while py[-1]*y<bound:
                py.append(py[-1]*y)
        
        res=set()
        for i in px:
            for j in py:
                if i+j<=bound:
                    res.add(i+j)
        return res