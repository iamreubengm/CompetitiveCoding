#3Sum With Multiplicity
'''
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.
As the answer can be very large, return it modulo 109 + 7.

Example:
    Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
    Output: 20
    Explanation: 
        Enumerating by the values (arr[i], arr[j], arr[k]):
        (1, 2, 5) occurs 8 times;
        (1, 3, 4) occurs 8 times;
        (2, 2, 4) occurs 2 times;
        (2, 3, 3) occurs 2 times.
'''

class Solution:
    def threeSumMulti(self,arr,target):
        res=0
        arr=sorted(arr)
        n=len(arr)
        for i,x in enumerate(arr):
            new_target=target-x
            j,k=i+1,n-1
            while j<k:
                if arr[j]+arr[k]<new_target:
                    j+=1
                elif arr[j]+arr[k]>new_target:
                    k-=1
                elif arr[j]!=arr[k]:
                    l=r=1
                    while j+1<k and arr[j]==arr[j+1]:
                        l+=1
                        j+=1
                    while k-1>j and arr[k]==arr[k-1]:
                        r+=1
                        k-=1
                    res+=(l*r)
                    res%=10**9+7
                    j+=1
                    k-=1
                else:
                    res+=(k-j+1)*(k-j)//2
                    res%=10**9+7
                    break
        return res