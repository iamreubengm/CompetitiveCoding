#Determine if Two Strings Are Close
'''
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example:
    Input: word1 = "cabbba", word2 = "abbccc"
    Output: true
    Explanation: You can attain word2 from word1 in 3 operations.
            Apply Operation 1: "cabbba" -> "caabbb"
            Apply Operation 2: "caabbb" -> "baaccc"
            Apply Operation 2: "baaccc" -> "abbccc"

Solution:
The strings are close if they have the same letters and their frequencies are the same
for swapping purposes. Thus we can use counters for this program and return if they are close
or not.
'''

from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1,c2=Counter(word1), Counter(word2)
        print(c1.values(),c2.values())
        return sorted(c2.values())==sorted(c1.values()) and c1.keys()==c2.keys()