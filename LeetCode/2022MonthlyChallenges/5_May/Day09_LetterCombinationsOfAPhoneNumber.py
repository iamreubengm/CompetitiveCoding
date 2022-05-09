#Letter Combinations of a Phone Number
'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''

class Solution:
    def letterCombinations(self,digits):               
        def backtracking(index,path):
            if len(path)==len(digits):
                res.append(''.join(path))
                return
            l=d[digits[index]]
            for x in l:
                path.append(x)
                backtracking(index+1,path)
                path.pop()
                
        if not digits:
            return []
        d={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}    
        res=[]
        backtracking(0,[])
        return res