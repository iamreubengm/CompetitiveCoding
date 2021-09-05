#Orderly Queue
'''
You are given a string s and an integer k. You can choose one of the first k letters of s and append it at the end of the string..
Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.

Example:
    Input: s = "cba", k = 1
    Output: "acb"
    Explanation: 
        In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
        In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".

    Input: s = "baaca", k = 3
    Output: "aaabc"
    Explanation: 
        In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
        In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".
'''

class Solution:
    def orderlyQueue(self,s,k):
        if k==1:
            m=s
            for i in range(len(s)):
                t=s[i:]+s[:i]
                if t<m:
                    m=t
            return m
        return ''.join(sorted(s))         