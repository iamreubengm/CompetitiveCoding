#Smallest String With A Given Numeric Value
'''
The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet,
so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.
The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values.
For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.
You are given two integers n and k. Return the lexicographically smallest string with length equal to n and
numeric value equal to k.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order,
that is: either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

Example:
    Input: n = 3, k = 27
    Output: "aay"
    Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is the smallest string with such a value and length equal to 3.

Solution:
The smallest string is derived by having as many a's or initial alphabets as possible in the beginning and as many z's or latter alphabets
towards the end of the string.
We can start by initialising all characters in the string to 'a'. We also subtract 'n' from 'k' as we have n a's in the string [a=1].
The from the end of the string, we replace the character with 'z' or the value of 'k' if it is less than 25 [z=25].
We change the value of 'k' accordingly.
Finally we join the array and return the string.
'''

class Solution:
    def getSmallestString(self,n,k):
        k-=n
        res=['a']*n
        i=n-1
        while i>=0 and k:
            res[i]=chr(ord(res[i])+min(k,25))
            k-=min(k,25)
            i-=1
        return ''.join(res)

