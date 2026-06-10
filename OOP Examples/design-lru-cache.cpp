#include<iostream>
#include<unordered_map>
using namespace std;

// the Node structure holds an extra integer key for implementation of LRU Cache
struct Node {
    int key, value;
    Node* next;
    Node* prev;
    Node(int k, int v) : key(k), value(v), next(nullptr), prev(nullptr) {}
};

class DoublyLinkedList {
protected:
    Node* head;
    Node* tail;
    
    // helper method to unlink a specific node
    void unlink(Node* node) {
        // relink the two neighbors of the given node
        if (node->prev) {
            node->prev->next = node->next;
        }
        else {
            head = node->next;
        }
        if (node->next) {
            node->next->prev = node->prev;
        }
        else {
            tail = node->prev;
        }
        // unlink the given node
        node->prev = nullptr;
        node->next = nullptr;
    }
    
    // helper method to link a given node at the tail of the list
    void linkAtTail(Node* node) {
        node->prev = tail;
        node->next = nullptr;
        if (tail) {
            tail->next = node;
        }
        else {
            head = node;
        }
        tail = node;
    }
    
    // helper method to link a given node at the head of the list
    void linkAtHead(Node* node) {
        node->next = head;
        node->prev = nullptr;
        if (head) {
            head->prev = node;
        }
        else {
            tail = node;
        }
        head = node;
    }

public:
    // constructor
    DoublyLinkedList(): head(nullptr), tail(nullptr) {}
    
    // destructor
    virtual ~DoublyLinkedList() {
        Node* curr = head;
        while (curr) {
            Node* next = curr->next;
            delete curr;
            curr = next;
        }
    }
    
    // method to add a new node at the end of the list
    void addToTail(int key, int data) {
        Node* node = new Node(key, data);
        if (!head) {
            head = tail = node;
        }
        else {
            linkAtTail(node);
        }
    }
    
    // method to add a new node at the beginning of the list
    void addToHead(int key, int data) {
        Node* node = new Node(key, data);
        if (!head) {
            head = tail = node;
        } 
        else {
            linkAtHead(node);
        }
    }
    
    // delete a node with a given key
    void deleteNode(int key) {
        Node* curr = head;
        while (curr) {
            if (curr->key == key) {
                unlink(curr);
                delete curr;
                return;
            }
            curr = curr->next;
        }
    }
    
    /*The two methods below will be useful for the implementation of LRU Cache*/
    // (1): move an existing node to the tail
    void moveToTail(Node* node) {
        if (node == tail) {
            return;
        }
        unlink(node);
        linkAtTail(node);
    }
    
    // (2): detache and return the head node
    // NOTE: the caller of this function must delete the node to avoid memory leaks
    Node* removeHead() {
        if (!head) {
            return nullptr;
        }
        Node* node = head;
        unlink(node);
        return node;
    }
};

class LRUCache : public DoublyLinkedList {
private:
    int capacity;
    int size;
    unordered_map<int, Node*> map; // maps key ---> node pointer for O(1) lookup
    
public:
    // constructor
    LRUCache(int capacity) : DoublyLinkedList(), capacity(capacity), size(0) {}
    
    // look up a node via the map, move the node to tail (since it becomes most recently used),
    // and return the value, all in O(1) time
    int get(int key) {
        if (map.find(key) == map.end()) {
            return -1; // not found
        }
        moveToTail(map[key]);
        return map[key]->value;
    }
    
    // update existing node or insert a new one
    // evicting the least recently used node if needed
    // all in O(1) time
    void put(int key, int value) {
        // if key already exists, update its value and mark it as most recently used
        if (map.find(key) != map.end()) {
            map[key]->value = value;
            moveToTail(map[key]);
        }
        // otherwise, add to the tail to mark as most recently used
        else {
            addToTail(key, value);
            map[key] = tail; // put the newly added node to the map
            size++;
            
            // check if we overshoot the size of the cache
            if (size > capacity) {
                Node *lru = removeHead();
                map.erase(lru->key);
                delete lru;
                size--;
            }
        }
    }
}; 

int main() {
    LRUCache lRUCache(2);
    lRUCache.put(1, 10); // cache: {1=10}
    lRUCache.put(2, 20); // cache: {1=10, 2=20}
    cout << lRUCache.get(1) << endl; // 10;   cache: {2=20, 1=10}
    lRUCache.put(3, 30); // evicts 2;  cache: {1=10, 3=30}
    cout << lRUCache.get(2) << endl; // -1  (evicted)
    lRUCache.put(4, 40); // evicts 1;  cache: {3=30, 4=40}
    cout << lRUCache.get(1) << endl; // -1  (evicted)
    cout << lRUCache.get(3) << endl; // 30
    cout << lRUCache.get(4) << endl; // 40
    return 0;
}