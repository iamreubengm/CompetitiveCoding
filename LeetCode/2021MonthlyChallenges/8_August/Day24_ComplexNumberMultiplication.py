#Complex Number Multiplication
'''
A complex number can be represented as a string on the form "real+imaginaryi" where:
    real is the real part and is an integer in the range [-100, 100].
    imaginary is the imaginary part and is an integer in the range [-100, 100].
    i2 == -1.
Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

Example:
    Input: num1 = "1+1i", num2 = "1+1i"
    Output: "0+2i"
    Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
'''

class Solution:
    def complexNumberMultiply(self,num1,num2):
        i1=num1.index("+")
        i2=num2.index("+")
        ar,ai=int(num1[:i1]),int(num1[i1+1:-1])
        br,bi=int(num2[:i2]),int(num2[i2+1:-1])
        return str(ar*br-ai*bi)+"+"+str(ar*bi+br*ai)+"i"