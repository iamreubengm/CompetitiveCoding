#Erect the Fence
'''
You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.
You are asked to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed.
Return the coordinates of trees that are exactly located on the fence perimeter.

Example:
    Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
    Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]
'''

class Solution:
    def outerTrees(self,trees):
        trees=sorted(map(tuple,trees),key=lambda x:(x[0],x[1]))
        
        def sign(o, a, b):
            return (a[0]-o[0])*(b[1]-o[1])-(b[0]-o[0]) *(a[1]-o[1])
        
        def build(trees):
            hull = []
            for p in trees:
                while len(hull)>=2 and sign(hull[-2],hull[-1],p)<0:
                    hull.pop()
                hull+=p,
            return hull
        
        return list(set(build(trees)+build(trees[::-1])))