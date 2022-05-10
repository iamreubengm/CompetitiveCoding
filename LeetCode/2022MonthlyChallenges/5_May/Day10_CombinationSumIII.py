#Combination Sum III
'''
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
    Only numbers 1 through 9 are used.
    Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Example:
    Input: k = 3, n = 7
    Output: [[1,2,4]]
    Explanation:
        1 + 2 + 4 = 7
        There are no other valid combinations.
'''

class Solution:
    def combinationSum3(self,k,n):
        self.res=[]
        self.back(k,n,[])
        return self.res
    
    def back(self,k,n,cur):
        if n<0 or k<0:
            return
        if not n and not k:
            self.res.append(cur)
        s=cur[-1]+1 if cur else 1
        for i in range(s,10):
            self.back(k-1,n-i,cur+[i])
            