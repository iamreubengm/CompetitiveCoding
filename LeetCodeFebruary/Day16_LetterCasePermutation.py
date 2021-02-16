#Letter Case Permutation
'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. You can return the output in any order.

Example:
Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
'''

class Solution:
    def letterCasePermutation(self,S):
        def backtrack(i,a):
            if i==len(S):
                self.res.append(a)
                return
            if S[i].isalpha():
                backtrack(i+1,a+S[i].lower())
            backtrack(i+1,a+S[i].upper())
        
        self.res=[]
        backtrack(0,"")
        return self.res
