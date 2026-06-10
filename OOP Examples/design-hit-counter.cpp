#include<iostream>
using namespace std;

struct Node {
    int key; // will use timestamps as keys for Hit Counter
    int value; // will use the frequencies of the hits as values
    Node* next;
    Node* prev;
    Node(int k, int v): key(k), value(v), next(nullptr), prev(nullptr) {}
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
    
    // helper method to link a given node at the beginning of the list
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
    
    // helper method to link a given node at the end of the list
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
    
    // add a new node to the beginning of the list
    void addToHead(int key, int value) {
        Node* node = new Node(key, value);
        if (!head) {
            head = tail = node;
        }
        else {
            linkAtHead(node);
        }
    }
    
    // add a new node to the end of the list
    void addToTail(int key, int value) {
        Node* node = new Node(key, value);
        if (!head) {
            head = tail = node;
        }
        else {
            linkAtTail(node);
        }
    }
    
    // delete a node from a given key
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
    
    // the method below will be useful for Hit Counter implementation
    // unlink the node at the beginning of the list and return this node
    // NOTE: the caller needs to remove the node to avoid memory leaks
    Node* removeHead() {
        if (!head) {
            return nullptr;
        }
        Node* node = head;
        unlink(node);
        return node;
    }
};

class HitCounter : public DoublyLinkedList {
private:
    int totalHits;
    
public:
    HitCounter(): DoublyLinkedList(), totalHits(0) {}
    
    // append a new timestamp node or increment the count if already exists, O(1) time
    void hit(int timestamp) {
        // if same timestamp as last hit, increment the count
        if (tail && tail->key == timestamp) {
            tail->value++;
        }
        // new timestamp, add to the end of the list
        else {
            addToTail(timestamp, 1);
        }
        totalHits++;
    }
    
    // get the total hits in time O(k) where k is the number of expired timestamp buckets to evict
    // amorized O(1) since each node is added and remove at most once
    int getHits(int timestamp) {
        // remove expired nodes from the beginning of the list
        while (head && head->key <= timestamp - 300) { // 300 is a fixed threshold
            Node* expired = removeHead();
            totalHits -= expired->value;
            delete expired;
        }
        return totalHits;
    }
};

int main() {
    HitCounter hitCounter;
    hitCounter.hit(1);
    hitCounter.hit(2);
    hitCounter.hit(3);
    cout << hitCounter.getHits(4)   << endl; // 3
    hitCounter.hit(300);
    cout << hitCounter.getHits(300) << endl; // 4
    cout << hitCounter.getHits(301) << endl; // 3
    return 0;
}