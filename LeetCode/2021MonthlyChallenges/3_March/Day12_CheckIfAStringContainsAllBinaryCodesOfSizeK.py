#Check If a String Contains All Binary Codes of Size K
'''
Given a binary string s and an integer k.
Return True if every binary code of length k is a substring of s. Otherwise, return False.

Example:
    Input: s = "00110110", k = 2
    Output: true
    Explanation: The binary codes of length 2 are "00", "01", "10" and "11".
                 They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.

Solution:
The simple solution is to use a set. We go through the string and store all sub-strings in the set.
The set ensures the sub-strings are not repeated. Once done, we check the number of unique sub-strings.
If that value is equal to 2^k, we return True.
'''

class Solution:
    def hasAllCodes(self,s,k):
        unique=set()
        for i in range(len(s)-k+1):
            unique.add(s[i:i+k])
        return len(unique)==2**k