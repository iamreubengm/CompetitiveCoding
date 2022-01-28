#Design Add and Search Words Data Structure
'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the WordDictionary class:
    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example:
    Input:
        ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
        [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    Output:
        [null,null,null,null,false,true,true,true]
    Explanation:
        WordDictionary wordDictionary = new WordDictionary();
        wordDictionary.addWord("bad");
        wordDictionary.addWord("dad");
        wordDictionary.addWord("mad");
        wordDictionary.search("pad"); // return False
        wordDictionary.search("bad"); // return True
        wordDictionary.search(".ad"); // return True
        wordDictionary.search("b.."); // return True
'''

class TrieNode:
    def __init__(self):
        self.children={}
        self.end=0

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self,word):
        root=self.root
        for x in word:
            root=root.children.setdefault(x,TrieNode())
        root.end=1

    def search(self,word):
        def dfs(node, i):
            if i==len(word):
                return node.end
            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child],i+1):
                        return True
            if word[i] in node.children:
                return dfs(node.children[word[i]],i+1)
            return False
        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
