#Numbers At Most N Given Digit Set
'''
Given an array of digits which is sorted in non-decreasing order. You can write numbers using each digits[i] as many times as we want.
For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.
Return the number of positive integers that can be generated that are less than or equal to a given integer n.

Example:
    Input: digits = ["1","3","5","7"], n = 100
    Output: 20
    Explanation: 
        The 20 numbers that can be written are:
        1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
'''

class Solution:
    def atMostNGivenDigitSet(self,digits,n):
        num=str(n)
        nlen=len(num)
        dlen=len(digits)
        res=sum(dlen**i for i in range(1,nlen))
        for i in range(nlen):
            j=0
            while j<dlen and digits[j][0]<num[i]:
                res+=dlen**(nlen-i-1)
                j+=1
            if j>=dlen or digits[j][0]!=num[i]:
                return res
        return res+1