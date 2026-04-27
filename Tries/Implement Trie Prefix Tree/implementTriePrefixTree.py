'''
Implementation of Trie data structure

APPROACH:
1. Key idea is: Trie is NOT A BINARY TREE - each node can have multiple children
2. Use a hashmap to store all the child nodes for fast look up
3. Make a TrieNode class to store the children hashmap & a boolean end marker to signify the
end of a word/string
3. Children hashmap keys = letter/character, values = actual TrieNode object

O(N) time complexity
'''
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False

class Trie:
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode()             
            curr = curr.children[word[i]]

        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for s in word:
            if s not in curr.children:
                return False
            curr = curr.children[s]
        
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for s in prefix:
            if s not in curr.children:
                return False
            curr = curr.children[s]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)