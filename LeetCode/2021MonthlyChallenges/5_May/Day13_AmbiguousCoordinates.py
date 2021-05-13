#Ambiguous Coordinates
'''
We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)". Then, we removed all commas, decimal points, and spaces, and ended up with the string s.
Return a list of strings representing all possibilities for what our original coordinates could have been.
Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number
that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it,so we never started with numbers like ".1".
The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example:
    Input: s = "(123)"
    Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

    Input: s = "(00011)"
    Output:  ["(0.001, 1)", "(0, 0.011)"]
    Explanation: 0.0, 00, 0001 or 00.01 are not allowed.

    Input: s = "(0123)"
    Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
'''

class Solution:
    def ambiguousCoordinates(self,s):
        def helper(s):
            res=[]
            if s=="0" or s[0]!="0":
                res.append(s)
            for i in range(1,len(s)):
                if(s[:i]=="0" or s[0]!="0") and s[-1]!="0":
                    res.append(s[:i]+"."+s[i:])
            return res
        res=[]
        for i in range(2,len(s)-1):
            l,r=helper(s[1:i]),helper(s[i:-1])
            for j in range(len(l)):
                for k in range(len(r)):
                    res.append("("+l[j]+", "+r[k]+")")
        return res
            