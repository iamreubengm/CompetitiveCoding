#Decode Ways II
'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:
    'A' -> "1"
    'B' -> "2"
    ...
    'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways).
For example, "11106" can be mapped into:
    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)
    Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
In addition to the mapping above, an encoded message may contain the '*' character, which can represent any digit from '1' to '9' ('0' is excluded).
For example, the encoded message "1*" may represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19".
Decoding "1*" is equivalent to decoding any of the encoded messages it can represent.
Given a string s containing digits and the '*' character, return the number of ways to decode it.
Since the answer may be very large, return it modulo 109 + 7.

Example:
    Input: s = "1*"
    Output: 18
    Explanation: The encoded message can represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19".
                 Each of these encoded messages have 2 ways to be decoded (e.g. "11" can be decoded to "AA" or "K").
                 Hence, there are a total of 9 * 2 = 18 ways to decode "1*".
'''

class Solution:
    def numDecodings(self,s):
        d1=[1,0,0]
        for x in s:
            d2=[0,0,0]
            if x=='*':
                d2[0]=9*d1[0]+9*d1[1]+6*d1[2]
                d2[1]=d1[0]
                d2[2]=d1[0]
            else:
                d2[0]=(x>'0')*d1[0]+d1[1]+(x<='6')*d1[2]
                d2[1]=(x=='1')*d1[0]
                d2[2]=(x=='2')*d1[0]
            d1=[i%(10**9+7) for i in d2]
        return d1[0]