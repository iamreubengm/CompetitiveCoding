#Interval List Intersections
'''
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj].
Each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.
A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval.
For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Example:
    Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
    Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
'''

class Solution:
    def intervalIntersection(self,firstList,secondList):
        i,j=0,0
        r=[]
        while i<len(firstList) and j<len(secondList):
            a_begin,a_end=firstList[i]
            b_begin,b_end=secondList[j]
            if a_begin<=b_end and b_begin<=a_end:
                r.append([max(a_begin,b_begin),min(a_end,b_end)])
            if a_end<=b_end:
                i+=1
            else:
                j+=1
        return r