class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        c = self.root

        for i in word:
            if i not in c.children:
                c.children[i] = TrieNode()
            c = c.children[i]

        c.isEnd = True

    def search(self, word: str) -> bool:
        c = self.root
        
        for i in word:
            if i not in c.children:
                return False
            c = c.children[i]
        
        return c.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        c = self.root
        
        for i in prefix:
            if i not in c.children:
                return False
            c = c.children[i]

        return True
        
        