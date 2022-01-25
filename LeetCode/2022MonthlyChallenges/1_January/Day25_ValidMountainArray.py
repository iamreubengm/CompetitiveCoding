#Valid Mountain Array
'''
Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example:
    Input: arr = [2,1]
    Output: false

    Input: arr = [0,3,2,1]
    Output: true
'''

class Solution:
    def validMountainArray(self,arr):
        l,r=0,len(arr)-1
        n=len(arr)
        while l+1<n and arr[l]<arr[l+1]:
            l+=1
        while r>0 and arr[r-1]>arr[r]:
            r-=1
        return 0<r==l<n-1