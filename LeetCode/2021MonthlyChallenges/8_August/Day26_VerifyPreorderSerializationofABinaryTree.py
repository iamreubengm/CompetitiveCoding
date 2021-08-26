#Verify Preorder Serialization of a Binary Tree
'''
One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value.
If it is a null node, we record using a sentinel value such as '#'.
Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.
It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.
You may assume that the input format is always valid.
For example, it could never contain two consecutive commas, such as "1,,3".
Note: You are not allowed to reconstruct the tree.

Example:
    Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    Output: true
'''

class Solution:
    def isValidSerialization(self,preorder):
        bt=preorder.split(',')
        n=1
        for node in bt:
            if n<=0:
                return False
            if node=="#":
                n-=1
            else:
                n+=1
        return n==0