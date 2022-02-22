#Excel Sheet Column Number
'''
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example:
    Input: columnTitle = "AB"
    Output: 28
'''

class Solution:
    def titleToNumber(self,columnTitle):
        res=0
        for i,x in enumerate(columnTitle[::-1]):
            res+=(ord(x)-ord('A')+1)*26**i
        return res