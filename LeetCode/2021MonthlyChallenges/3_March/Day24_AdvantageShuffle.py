#Advantage Shuffle
'''
Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].
Return any permutation of A that maximizes its advantage with respect to B.

Example:
    Input: A = [2,7,11,15], B = [1,10,4,11]
    Output: [2,11,7,15]
'''

class Solution:
    def advantageCount(self,A,B):
        n=len(A)
        A=sorted(A)[::-1]
        B=sorted([(num, i) for i, num in enumerate(B)])[::-1]
        res=[-1]*n
        l,r=0,n-1
        
        for x,i in B:
            if A[l]>x:
                res[i]=A[l]
                l+=1
            else:
                res[i]=A[r]
                r-=1
                
        return res