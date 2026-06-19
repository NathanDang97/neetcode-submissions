from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end_of_word = False

# prefix tree + dfs solution, O(n) for all operations besides constructors, 
# O(t + n) space where t is the total number of trie nodes
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i] # current character
                # if c is not the wildcard character, do regular character matching 
                if c != '.':
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
                # otherwise, try all possible children nodes
                else:
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False # this means no valid path found
            return curr.end_of_word

        return dfs(0, self.root)
                    
