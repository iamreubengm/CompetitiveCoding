#Push Dominoes
'''
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.
You are given a string dominoes representing the initial state where:
    dominoes[i] = 'L', if the ith domino has been pushed to the left,
    dominoes[i] = 'R', if the ith domino has been pushed to the right, and
    dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

Example:
    Input: dominoes = "RR.L"
    Output: "RR.L"
    Explanation: The first domino expends no additional force on the second domino.
'''

class Solution:
    def pushDominoes(self,dominoes):
        dominoes="L"+dominoes+"R"
        res=''
        p=0
        for i in range(1,len(dominoes)):
            d=i-p-1
            if dominoes[i]=='.':
                continue
            if dominoes[i]==dominoes[p]:
                res+=dominoes[i]*d
            elif dominoes[i]=='L' and dominoes[p]=='R':
                r=d%2
                q=d//2
                res+="R"*q+'.'*r+'L'*q
            else:
                res+='.'*d
            res+=dominoes[i]
            p=i
        return res[:-1]
            