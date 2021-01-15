#Get Maximum In Generated Array
'''
You are given an integer n. An array nums of length n + 1 is generated in the following way:
    nums[0] = 0
    nums[1] = 1
    nums[2 * i] = nums[i] when 2 <= 2 * i <= n
    nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
Return the maximum integer in the array nums​​​.

Example:
    Input: n = 7
    Output: 3
    Explanation: According to the given rules:
      nums[0] = 0
      nums[1] = 1
      nums[(1 * 2) = 2] = nums[1] = 1
      nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
      nums[(2 * 2) = 4] = nums[2] = 1
      nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
      nums[(3 * 2) = 6] = nums[3] = 2
      nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
    Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is 3.
    
Solution:
Start with an array [0,1]. Then based on if the number is even or odd, use the given conditions
to generate the other elements of the array. Finally return the max element in the array
 
'''

class Solution:
    def getMaximumGenerated(self,n):
        if n==0:
            return 0
        arr=[0,1]
        for i in range(2,n+1):
            if i%2==0:
                arr.append(arr[i//2])
            else:
                arr.append(arr[i//2]+arr[(i//2)+1])
        return max(arr)