class TrieNode:
    # solution using a list to represent the children
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            # create a new child of not exist
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()

            curr = curr.children[idx]

        # mark end_of_word to True after processing the input word
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        # start from root and return False if some child is not found
        # otherwise return True
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        # similar idea as search method
        curr = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        return True
        
        