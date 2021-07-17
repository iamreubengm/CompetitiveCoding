#Three Equal Parts
'''
You are given an array arr which consists of only zeros and ones, divide the array into three non-empty parts such that all of these parts represent the same binary value.
If it is possible, return any [i, j] with i + 1 < j, such that:
    arr[0], arr[1], ..., arr[i] is the first part,
    arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
    arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
    All three parts have equal binary values.
If it is not possible, return [-1, -1].
Note that the entire part is used when considering what binary value it represents.
For example, [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.

Example:
    Input: arr = [1,0,1,0,1]
    Output: [0,3]
'''

class Solution:
    def threeEqualParts(self,arr):
        n=len(arr)
        ind=[i for i in range(n) if arr[i]==1]
        m=len(ind)
        if m == 0:
            return [0, 2]
        if m%3!=0:
            return [-1, -1]
        p1,p2=ind[0],ind[m//3-1]
        p3,p4=ind[m//3],ind[2*m//3-1]
        p5,p6=ind[2*m//3],ind[-1]
        part1,part2,part3=arr[p1:p2+1],arr[p3:p4+1],arr[p5:p6+1]
        
        if part1 != part2 or part2 != part3:
            return [-1, -1]
        l1=p3-p2-1
        l2=p5 - p4 - 1
        l3=n-p6-1
        
        if l3>l2 or l3>l1:
            return [-1, -1]
        return [p2+l3,p4+l3+1]