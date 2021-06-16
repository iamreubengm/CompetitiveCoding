#Generate Parentheses
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
'''

class Solution:
    def generateParenthesis(self,n):
        res=[]
        def backtrack(s,left,right):
            if len(s)==2*n:
                res.append(''.join(s))
                return
            if left<n:
                s.append("(")
                backtrack(s,left+1,right)
                s.pop()
            if right<left:
                s.append(")")
                backtrack(s,left,right+1)
                s.pop()
        backtrack([],0,0)
        return res