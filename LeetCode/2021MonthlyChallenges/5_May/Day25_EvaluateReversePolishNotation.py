#Evaluate Reverse Polish Notation
'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
Note that division between two integers should truncate toward zero.
It is guaranteed that the given RPN expression is always valid.
That means the expression would always evaluate to a result, and there will not be any division by zero operation.

Example:
    Input: tokens = ["2","1","+","3","*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9

    Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22
    Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
                = ((10 * (6 / (12 * -11))) + 17) + 5
                = ((10 * (6 / -132)) + 17) + 5
                = ((10 * 0) + 17) + 5
                = (0 + 17) + 5
                = 17 + 5
                = 22
'''
class Solution:
    def evalRPN(self,tokens):
        stack=[]
        
        def calc(a,b,o):
            if o=='+':
                return a+b
            elif o=='-':
                return b-a
            elif o=='*':
                return a*b
            else:
                return int(b/a)
            
        for x in tokens:
            if x not in "+-*/":
                stack.append(int(x))
            else:
                stack.append(calc(stack.pop(),stack.pop(),x))
        return stack[-1]
        
