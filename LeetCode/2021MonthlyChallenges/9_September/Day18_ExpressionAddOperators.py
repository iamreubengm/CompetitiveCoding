#Expression Add Operators
'''
Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*'
between the digits of num so that the resultant expression evaluates to the target value.

Example:
    Input: num = "123", target = 6
    Output: ["1*2*3","1+2+3"]
'''

class Solution:
    def addOperators(self,num,target):
        def search(i,s,l):
            if i>=n:
                if eval(s)==target:
                    res.append(s)
                return
            search(i+1,s+"+"+num[i],num[i])
            search(i+1,s+"-"+num[i],num[i])
            search(i+1,s+"*"+num[i],num[i])
            if l!='0':
                search(i+1,s+num[i],l)
        res=[]
        n=len(num)
        search(1,num[0],num[0])
        return res