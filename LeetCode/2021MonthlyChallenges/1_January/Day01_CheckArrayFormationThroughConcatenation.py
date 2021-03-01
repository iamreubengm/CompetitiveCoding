#Check Array Formation Through Concatenation
'''Given an array of distinct integers 'arr', and an array of integer arrays 'pieces
#Check if 'arr' can be formed by concatenating arrays in 'pieces' in any order
#Integers in the array in 'pieces' cannot be reordered

Solution:
Consider a dictionary where the key is the first element of every array in pieces,
and the value is the individual array.
Go through 'arr', and if the element is a key in the dictionary, add the entire array
to a new array 'res'.
Compare 'res' and 'arr': If they are equal, the objective can be accomplished."

'''
class Solution:
    def canFormArray(self, arr, pieces):
        res=[]
        d={x[0]:x for x in pieces}
        for i in arr:
            if i in d:
                res+=d[i]
        return res==arr
