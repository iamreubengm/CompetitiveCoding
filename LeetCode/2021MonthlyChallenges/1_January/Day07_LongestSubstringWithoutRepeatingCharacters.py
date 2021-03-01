#Longest Substring Without Repeating Characters
'''
Given a string s, find the length of the longest substring without repeating characters.

Solution:
Use a hashmap to store the index of the most recent appearance of a character.
If the character already has been seen, the starting index is incremented.
Otherwise the max length is either taken as the current max or the length of
the substring currently being checked.
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        d={}
        start_index=0
        maxlen=0
        for i,x in enumerate(s):
            if x in d and start_index<=d[x]:
                start_index=d[x]+1
            else:
                maxlen=max(maxlen,i-start_index+1)
            d[x]=i
        return maxlen