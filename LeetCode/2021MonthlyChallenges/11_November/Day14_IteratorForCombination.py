#Iterator for Combination
'''
Design the CombinationIterator class:
    CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
    next() Returns the next combination of length combinationLength in lexicographical order.
    hasNext() Returns true if and only if there exists a next combination.

Example:
    Input
        ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
        [["abc", 2], [], [], [], [], [], []]
    Output
        [null, "ab", true, "ac", true, "bc", false]

    Explanation
        CombinationIterator itr = new CombinationIterator("abc", 2);
        itr.next();    // return "ab"
        itr.hasNext(); // return True
        itr.next();    // return "ac"
        itr.hasNext(); // return True
        itr.next();    // return "bc"
        itr.hasNext(); // return False
'''

class CombinationIterator:

    def __init__(self,characters,combinationLength):
        self.s=characters
        self.c=[i for i in range(combinationLength-1)]+[combinationLength-2]

    def next(self) -> str:
        for i in range(1,len(self.c)+1):
            if self.c[-i]<len(self.s)-i:
                self.c[-i]+=1
                while i!=1:
                    self.c[-i+1]=self.c[-i]+1
                    i-=1
                break
        return ''.join([self.s[x] for x in self.c])

    def hasNext(self) -> bool:
        return self.c[0]!=len(self.s)-len(self.c)

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()