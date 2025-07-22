class TrieNode:
    def __init__(self):
    
        self.childs = {}
        self.IsEnd = False


class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.childs:
                curr.childs[c]=TrieNode()
                curr = curr.childs[c]
            else:
                curr = curr.childs[c]
        curr.IsEnd = True


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.childs:
                return False
            curr = curr.childs[c]
        return curr.IsEnd
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.childs:
                return False
            curr = curr.childs[c]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)