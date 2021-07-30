#Map Sum Pairs
'''
Implement the MapSum class:
    MapSum() Initializes the MapSum object.
    void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
    int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.

Example:
Input
    ["MapSum", "insert", "sum", "insert", "sum"]
    [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
    [null, null, 3, null, 5]
Explanation
    MapSum mapSum = new MapSum();
    mapSum.insert("apple", 3);  
    mapSum.sum("ap");           // return 3 (apple = 3)
    mapSum.insert("app", 2);    
    mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
'''

import collections

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d={}
        self.s=collections.Counter()

    def insert(self, key: str, val: int) -> None:
        delta=val-self.d.get(key,0)
        self.d[key]=val
        for i in range(len(key)+1):
            pref=key[:i]
            self.s[pref]+=delta

    def sum(self, prefix: str) -> int:
        return self.s[prefix]


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)