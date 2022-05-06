#Remove All Adjacent Duplicates in String II
'''
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them,
causing the left and the right side of the deleted substring to concatenate together.
We repeatedly make k duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Example:
    Input: s = "deeedbbcccbdaa", k = 3
    Output: "aa"
    Explanation: 
        First delete "eee" and "ccc", get "ddbbbdaa"
        Then delete "bbb", get "dddaa"
        Finally delete "ddd", get "aa"
'''

class Solution:
    def removeDuplicates(self,s,k):
        stack=[['#',0]]
        for x in s:
            if stack[-1][0]==x:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([x,1])
        return ''.join(c*k for c,k in stack)