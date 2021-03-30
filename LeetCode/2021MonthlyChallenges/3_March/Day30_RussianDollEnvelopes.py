#Russian Doll Envelopes
'''
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.
One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height
of the other envelope.
Return the maximum number of envelopes can you Russian doll (i.e., put one inside the other).
Note: You cannot rotate an envelope.

Example:
    Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
    Output: 3
    Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
'''

from bisect import bisect_left
class Solution:
    def maxEnvelopes(self,envelopes):
        envelopes=sorted(envelopes, key=lambda x:(x[0],-x[1]))
        dp=[]
        for width,height in envelopes:
            left=bisect_left(dp,height)
            if left==len(dp):
                dp.append(height)
            else:
                dp[left] = height
        return len(dp)