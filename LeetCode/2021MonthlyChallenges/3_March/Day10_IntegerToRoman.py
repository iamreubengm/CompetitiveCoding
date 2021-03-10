#Integer to Roman
'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
            Symbol       Value
            I             1
            V             5
            X             10
            L             50
            C             100
            D             500
            M             1000
            
For example, 2 is written as II in Roman numeral, just two one's added together.
12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Solution:
One solution to this problem is to use a dictionary with all the symbols, including 
the instances where subtraction is used. Then go through each element and while that
element is smaller than 'num', we append the symbol to the result and subtract it from 'num'.
This gives the correct roman representation.

A second solution is to use the same dictionary 'd', but this time, we append each symbol n times
to the result, where n is the initial number divided by the integer value of each symbol. 
Thus 2002 will have 2 M's, as 2002//1000 is 2. At each step we perform modulo to reduce the number based
on the symbols appended. 
'''

class Solution:
    def intToRoman(self,num):
        res=''
        d = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        for x in d:
            while num>=x:
                num-=x
                res+=d[x]
        return res
    
    def intToRoman2(self,num):
        res=''
        d = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        for i,x in d.items():
            res+=x*(num//i)
            num%=i
        return res
