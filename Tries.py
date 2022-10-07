class Trie:

    def __init__(self):
        self.head = {}

    def insert(self, word: str) -> None:
        cur = self.head
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['*'] = True

    def search(self, word: str) -> bool:
        cur = self.head
        for char in word:
            if char not in cur:
                return False
            else:
                cur = cur[char]
        if '*' in cur and cur['*'] == True:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for char in prefix:
            if char not in cur:
                return False
            else:
                cur = cur[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
