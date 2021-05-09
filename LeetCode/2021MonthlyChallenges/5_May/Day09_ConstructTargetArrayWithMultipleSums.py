#Construct Target Array With Multiple Sums
'''
Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
You may repeat this procedure as many times as needed.
Return True if it is possible to construct the target array from A otherwise return False.

Example:
    Input: target = [9,3,5]
    Output: true
    Explanation: Start with [1, 1, 1] 
                [1, 1, 1], sum = 3 choose index 1
                [1, 3, 1], sum = 5 choose index 2
                [1, 3, 5], sum = 9 choose index 0
                [9, 3, 5] Done

    Input: target = [1,1,1,2]
    Output: false
    Explanation: Impossible to create target array from [1,1,1,1].
'''

class Solution:
    def isPossible(self,target):
        totalSum=sum(target)
        target=[-i for i in target]
        heapq.heapify(target)
        while True:
            x=-heapq.heappop(target)
            totalSum-=x
            if x==1 or totalSum==1:
                return True
            if x<totalSum or not totalSum or not x%totalSum:
                return False
            x%=totalSum
            totalSum+=x
            heapq.heappush(target,-x)