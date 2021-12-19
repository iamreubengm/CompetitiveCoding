#Decode String
'''
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Example:
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"

    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"
'''

class Solution:
    def decodeString(self,s):
        i,n=0,0
        stack=['']
        while i<len(s):
            if s[i].isdigit():
                n=n*10+int(s[i])
            elif s[i]=='[':
                stack.append(n)
                n=0
                stack.append('')
            elif s[i]==']':
                s1=stack.pop()
                r=stack.pop()
                s2=stack.pop()
                stack.append(s2+s1*r)
            else:
                stack[-1]+=s[i]
            i+=1
        return ''.join(stack)