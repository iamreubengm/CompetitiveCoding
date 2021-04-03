#Longest Valid Parentheses
'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example:

    Input: s = "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()".
       
    Input: s = ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()".

Solution:
We use a stack to solve this problem. Every time we encounter a '(', we push it's index to the stack.
When we get a ')', we pop the last element. If our stack is empty, it means that we have an extra ')'. So we
push it's index to the stack which could be the start of the next sequence. If it is not empty, we update the
longest variable.
'''

class Solution:
    def longestValidParentheses(self,s):
        stack=[]
        longest=0
        stack.append(-1)
        for i,x in enumerate(s):
            if x=='(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                else:
                    longest=max(longest,i-stack[-1])
        return longest
