#Accounts Merge
'''
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts.
Note that even if two accounts have the same name, they may belong to different people as people could have the same name.
A person can have any number of accounts initially, but all of their accounts definitely have the same name.
After merging the accounts, return the accounts in the following format:
    the first element of each account is the name, and the rest of the elements are emails in sorted order.
    The accounts themselves can be returned in any order.

Example:
Input:
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output:
    [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
    The first and second John's are the same person as they have the common email "johnsmith@mail.com".
    The third John and Mary are different people as none of their email addresses are used by other accounts.
    We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
    ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
'''

from collections import defaultdict

class Solution:
    def accountsMerge(self,accounts):
        def dfs(email):
            seen.add(email)
            emailList=[email]
            for e in g[email]:
                if e not in seen:
                    emailList.extend(dfs(e))
            return emailList
        
        g,seen,res=defaultdict(list),set(),[]
        for x in accounts:
            for i in range(2,len(x)):
                g[x[i]].append(x[i-1])
                g[x[i-1]].append(x[i])       
        for x in accounts:
            if x[1] not in seen:
                res.append([x[0]]+sorted(dfs(x[1])))
        return res