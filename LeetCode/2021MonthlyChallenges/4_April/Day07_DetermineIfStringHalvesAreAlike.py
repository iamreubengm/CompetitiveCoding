#Determine if String Halves Are Alike
'''
You are given a string s of even length. Split this string into two halves of equal lengths,
and let a be the first half and b be the second half.
Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
Notice that s contains uppercase and lowercase letters.
Return true if a and b are alike. Otherwise, return false.

Example:
    Input: s = "book"
    Output: true
    Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
        
    Input: s = "textbook"
    Output: false
    Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
                Notice that the vowel o is counted twice.

Solution:
This is a simple problem where we first convert all characters to lowercase.
We then traverse the first part of the string, and if the character is a vowel (in the 'vowel' string),
we increment a count variable. We then go through the second half of the string and decrement the count
whenever we encounter a vowel. Finally we True if the count is 0, and False otherwise.
'''

class Solution:
    def halvesAreAlike(self,s):
        s=s.lower()
        vowels='aeiou'
        count=0
        for x in s[:len(s)//2]:
            if x in vowels:
                count+=1
        for x in s[len(s)//2:]:
            if x in vowels:
                count-=1
        return count==0