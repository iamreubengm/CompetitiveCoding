#Search Suggestions System
'''
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
Return list of lists of the suggested products after each character of searchWord is typed. 

Example:
    Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
    Output: [
            ["mobile","moneypot","monitor"],
            ["mobile","moneypot","monitor"],
            ["mouse","mousepad"],
            ["mouse","mousepad"],
            ["mouse","mousepad"]
            ]
    Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
                After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
                After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
'''

class Solution:
    def suggestedProducts(self,products,searchWord):
        products.sort()
        n=len(products)
        res,inp=[],''
        for x in searchWord:
            t=[]
            inp+=x
            index=self.binarySearch(products,inp)
            for i in range(index,min(n,index+3)):
                if products[i].startswith(inp):
                    t.append(products[i])
            res.append(t)
        return res
            
        
    def binarySearch(self,products,inp):
        l,r=0,len(products)
        while l<r:
            m=l+(r-l)//2
            if products[m]<inp:
                l=m+1
            else:
                r=m
        return l