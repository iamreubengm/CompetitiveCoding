#Group Anagrams
'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

class Solution:
    def groupAnagrams(self, strs):
        d={}
        for x in strs:
            l=tuple(sorted(x))
            if l in d:
                d[l].append(x)
            else:
                d[l]=[x]
        return d.values()