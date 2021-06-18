#Range Sum Query - Mutable
'''
Given an integer array nums, handle multiple queries of the following types:
Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:
    NumArray(int[] nums) Initializes the object with the integer array nums.
    void update(int index, int val) Updates the value of nums[index] to be val.
    int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example:
    Input
        ["NumArray", "sumRange", "update", "sumRange"]
        [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
    Output
        [null, 9, null, 8]
    Explanation
        NumArray numArray = new NumArray([1, 3, 5]);
        numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
        numArray.update(1, 2);   // nums = [1, 2, 5]
        numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
'''

class BIT:
    def __init__(self,n):
        self.sums=[0]*(n+1)
    
    def update(self,i,d):
        while i<len(self.sums):
            self.sums[i]+=d
            i+=i&(-i)
    
    def query(self,i):
        res = 0
        while i>0:
            res+=self.sums[i]
            i-=i&(-i)
        return res

class NumArray:

    def __init__(self,nums):
        self.bit=BIT(len(nums))
        for i, x in enumerate(nums):
            self.bit.update(i+1,x)
        self.nums=[0]+nums

    def update(self,index,val):
        self.bit.update(index+1,val-self.nums[index+1])
        self.nums[index+1]=val

    def sumRange(self,left,right):
        return self.bit.query(right+1) - self.bit.query(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)