#Design HashMap
'''
Design a HashMap without using any built-in hash table libraries.
Implement the MyHashMap class:
    MyHashMap() initializes the object with an empty map.
    void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
    int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
    void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

Example:
    Input
        ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
        [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
    Output
        [null, null, null, 1, -1, null, 1, null, -1]
    Explanation
        MyHashMap myHashMap = new MyHashMap();
        myHashMap.put(1, 1); // The map is now [[1,1]]
        myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
        myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
        myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
        myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
        myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
        myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
        myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
'''

class ListNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.h=[None]*self.size 

    def put(self,key,value):
        """
        value will always be non-negative.
        """
        index=key%self.size 
        if self.h[index]==None:
            self.h[index]=ListNode(key,value)
        else:
            cur=self.h[index]
            while True:
                if cur.key == key:
                    cur.value = value
                    return 
                if cur.next == None: break
                cur = cur.next 
            cur.next = ListNode(key, value)

    def get(self,key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index=key%self.size 
        cur=self.h[index]
        while cur:
            if cur.key==key:
                return cur.value 
            else:
                cur=cur.next
        return -1

    def remove(self,key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index=key%self.size 
        cur=prev =self.h[index]
        if not cur: 
            return 
        if cur.key==key:
            self.h[index]=cur.next
        else:
            cur=cur.next
            while cur:
                if cur.key==key:
                    prev.next=cur.next 
                    break
                else:
                    prev,cur=prev.next,cur.next
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)