#Super Palindromes
'''
Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.
Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].

Example:
    Input: left = "4", right = "1000"
    Output: 4
    Explanation: 4, 9, 121, and 484 are superpalindromes.
    Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
'''

class Solution:
    def superpalindromesInRange(self,left,right):
        l,r=int(left),int(right)
        res=0
        
        def reverse(x):
            rev=0
            while x:
                rev=(10*rev)+(x%10)
                x//=10
            return rev

        def is_palindrome(x):
            return x==reverse(x)

        for i in range(100000):
            s=str(i)
            t=s+s[-2::-1]
            v=int(t)**2
            if v>r:
                break
            if v>=l and is_palindrome(v):
                res+=1
                
        for i in range(100000):
            s=str(i)
            t=s+s[::-1]
            v=int(t)**2
            if v>r:
                break
            if v>=l and is_palindrome(v):
                res+=1

        return res