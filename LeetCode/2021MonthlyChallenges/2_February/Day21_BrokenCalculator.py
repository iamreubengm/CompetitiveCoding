#Broken Calculator
'''
On a broken calculator that has a number showing on its display, we can perform two operations:
Double: Multiply the number on the display by 2, or;
Decrement: Subtract 1 from the number on the display.
Initially, the calculator is displaying the number X.

Return the minimum number of operations needed to display the number Y.

Example:
    Input: X = 3, Y = 10
    Output: 3
    Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.
    
    Input: X = 1024, Y = 1
    Output: 1023
    Explanation: Use decrement operations 1023 times.

Solution:
We use a greedy approach, where we start with Y and divide it by 2 till it becomes less than X.
An even nuumber has a straightforward divide by 2 operation, but an odd number needs to be incremented 
by one, then divided by 2. Line 5 takes care of these steps.
Finally, we return the result, added to the difference between X and Y (Y is now less than X).
'''

class Solution:
    def brokenCalc(self,X,Y):
        res=0
        while Y>X:
            res+=1+Y%2
            Y=(Y+1)//2
        return res+(X-Y)