#Kth Largest Element in a Stream
'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
Implement KthLargest class:
    KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
    int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Example:
    Input
        ["KthLargest", "add", "add", "add", "add", "add"]
        [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    Output
        [null, 4, 5, 5, 8, 8]
    Explanation
        KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
        kthLargest.add(3);   // return 4
        kthLargest.add(5);   // return 5
        kthLargest.add(10);  // return 5
        kthLargest.add(9);   // return 8
        kthLargest.add(4);   // return 8
'''

from heapq import heapify,heappush,heappop

class KthLargest:

    def __init__(self,k,nums):
        self.h=nums
        self.k=k
        heapify(self.h)
        while len(self.h)>k:
            heappop(self.h)
        

    def add(self,val):
        heappush(self.h,val)
        if len(self.h)>self.k:
            heappop(self.h)
        return self.h[0]
            

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)