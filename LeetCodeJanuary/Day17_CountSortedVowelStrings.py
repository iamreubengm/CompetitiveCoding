#Count Sorted Vowel Strings
'''
Given an integer n, return the number of strings of length n that consist only of vowels
(a, e, i, o, u) and are lexicographically sorted.
A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before
s[i+1] in the alphabet.

Example:
    Input: n = 2
    Output: 15
    Explanation: The 15 sorted strings that consist of vowels only are
                ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
                Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
Solution:
The mathematical solution would use the permutations formula to result in a final formula
as seen in the function, thus taking O(1) complexity.

A trivial solution can be obtained by considering n=2:
The acceptable second letter when the first letter is 'a' is any of the vowels (=5)
Similarly when the first letter is e, the acceptable second letters are [e,i,o,u] (=4)
Thus, the total number of acceptable strings would be 5+4+3+2+1= 15
Aplying this logic, we can create a trivial solution.
'''
class Solution:
    def countVowelStringsMath(self,n):
        return ((n+1)*(n+2)*(n+3)*(n+4))//24
    
    def countVowelStringsTrivial(self,n):
        res=0
        for i in range(n+2):
            s=0
            for j in range(i+1):
                s+=j
                res+=s
        return res