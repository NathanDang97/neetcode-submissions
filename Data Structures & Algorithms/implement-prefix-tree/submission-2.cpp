class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool endOfWord;

    // constructor
    TrieNode() : endOfWord(false) {}

    // destructor
    ~TrieNode() {
        for (auto& [ch, node] : children) {
            delete node;  // triggers child's destructor recursively
        }
    }
};

// solution using hashmap to represent the children
// O(n) time and space
class PrefixTree {
private:
    TrieNode* root;
public:
    // constructor
    PrefixTree() {
        root = new TrieNode();
    }

    // destructor
    ~PrefixTree() {
        delete root;  // cascades through the whole tree
    }
    
    void insert(string word) {
        TrieNode* curr = root;
        for (char c : word) {
            if (curr->children.find(c) == curr->children.end()) {
                curr->children[c] = new TrieNode();
            }
            curr = curr->children[c];
        }
        curr->endOfWord = true;
    }
    
    bool search(string word) {
        TrieNode* curr = root;
        for (char c : word) {
            if (curr->children.find(c) == curr->children.end()) {
                return false;
            }
            curr = curr->children[c];
        }
        return curr->endOfWord;
    }
    
    bool startsWith(string prefix) {
        TrieNode* curr = root;
        for (char c : prefix) {
            if (curr->children.find(c) == curr->children.end()) {
                return false;
            }
            curr = curr->children[c];
        }
        return true;
    }
};
