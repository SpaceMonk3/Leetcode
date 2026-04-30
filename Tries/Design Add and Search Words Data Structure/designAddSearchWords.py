# Same idea and approach as Implement Tire (Prefix Trie)
# Only thing different is the need to handle the wildcard '.' by using recursive DFS - so all possible branches are visited to check for valid word matches

from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not curr.children[c]:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(word: str, curr: TrieNode) -> bool:     
            for i in range(len(word)):
                if word[i] is '.':
                    for value in curr.children.values():
                        if dfs(word[i+1:], value):
                            return True
                    return False
                if not curr.children[word[i]]:
                    return False
                curr = curr.children[word[i]]

            return curr.isEnd
        
        return dfs(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)