#Reconstruct Original Digits from English
'''
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.
Note:
    Input contains only lowercase English letters.
    Input is guaranteed to be valid and can be transformed to its original digits.
    That means invalid inputs such as "abc" or "zerone" are not permitted.
    Input length is less than 50,000.
    
Example:
    Input: "owoztneoer"
    Output: "012"
    
    Input: "fviefuro"
    Output: "45"

Solution:
Looking at the numbers, we find that 0,2,4,6,8 all have unique letters not found in any other number [z,w,u,x,g].
After this, the remaining odd numbers have unique letters [o,t,f,s,i]. We store this information in a dictionary.
We go in the order of even first then odd. For each number, we check if the unique letter is present in the counter of's'.
If so, we update the 'res' list, and remove all the letters in the number from the counter.
We finally return the res list as a string.
'''

class Solution:
    def originalDigits(self,s):
        count=Counter(s)
        num_words={0: ['zero','z'], 1: ['one','o'], 2: ['two','w'], 3: ['three','t'], 4: ['four','u'],
               5: ['five','f'], 6: ['six','x'], 7: ['seven','s'], 8: ['eight','g'], 9: ['nine','i']}
        res=[0]*10
        
        for i in [0,2,4,6,8,1,3,5,7,9]:
            w=num_words[i][0]
            u=num_words[i][1]
            if count[u]:
                res[i]=count[u]
            for x in w:
                count[x]-=res[i]
        return ''.join([str(i)*res[i] for i in range(10)])