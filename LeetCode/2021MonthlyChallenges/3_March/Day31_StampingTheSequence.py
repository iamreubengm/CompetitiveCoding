#Stamping The Sequence
'''
You want to form a target string of lowercase letters.
At the beginning, your sequence is target.length '?' marks.You also have a stamp of lowercase letters.
On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the
corresponding letter from the stamp.  You can make up to 10 * target.length turns.

For example, if the initial sequence is "?????", and your stamp is "abc",  then you may make "abc??", "?abc?", "??abc" in the first turn. 
(Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)
If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped at each turn.
If the sequence is not possible to stamp, return an empty array.

For example, if the sequence is "ababc", and the stamp is "abc", then we could return the answer [0, 2],
corresponding to the moves "?????"-> "abc??" -> "ababc".

Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within 10 * target.length moves.
Any answers specifying more than this number of moves will not be accepted.
'''

class Solution:
    def movesToStamp(self,stamp,target):
        n,m=len(target),len(stamp)
        t,s=list(target),list(stamp)
        res=[]
        
        def check(i):
            changed=False
            for j in range(m):
                if t[i+j]=='?':
                    continue
                if t[i+j]!=s[j]:
                    return False
                changed = True
            if changed:
                t[i:i+m]=['?']*m
                res.append(i)
            return changed

        changed=True
        while changed:
            changed=False
            for i in range(n-m+1):
                changed|=check(i)
        if t==['?']*n:
            return res[::-1]
        return []

