#Check If Two String Arrays are Equivalent
'''
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
A string is represented by an array if the array elements concatenated in order forms the string.

Example:
    Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
    Output: true
    Explanation:
        word1 represents string "ab" + "c" -> "abc"
        word2 represents string "a" + "bc" -> "abc"
        The strings are the same, so return true.
        
Solution:
This is a very simple problem that can be solved by concatenating the Strings
in both arrays and by performing a simple equality check.
'''

class Solution:
    def arrayStringsAreEqual(self,word1, word2):
        return ''.join(word1)==''.join(word2)