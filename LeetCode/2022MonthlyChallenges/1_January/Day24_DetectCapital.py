#Detect Capital
'''
We define the usage of capitals in a word to be right when one of the following cases holds:
    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example:
    Input: word = "USA"
    Output: true

    Input: word = "FlaG"
    Output: false
'''

class Solution:
    def detectCapitalUse(self,word):
        n=len(word)
        count=0
        for x in word:
            count+=x.isupper()
        if count==n or count==0 or (count==1 and word[0].isupper()):
            return True
        return False