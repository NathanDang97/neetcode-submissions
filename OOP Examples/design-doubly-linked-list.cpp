#include <iostream>
using namespace std;

struct Node {
    int value;
    Node* next;
    Node* prev; // pointer to the previous node
    Node(int x) : value(x), next(nullptr), prev(nullptr) {}
};

class DoublyLinkedList {
private:
    Node* head;
    Node* tail;
public:
    DoublyLinkedList() : head(nullptr), tail(nullptr) {}
    ~DoublyLinkedList() {
        Node *curr = head;
        while (curr) {
            Node* nextNode = curr->next;
            delete curr;
            curr = nextNode;
        }
    }
    
    // add a node to the end of the list, O(1) time
    void append(int data) {
        Node* node = new Node(data);
        if (!head) {
            head = tail = node;
        }
        else {
            tail->next = node; // link current tail forward to the new node
            node->prev = tail; // link the new node backward to the current tail
            tail = node; // update the new tail
        }
    }
    
    // add a node to the beginning of the list, O(1) time
    void addFront(int data) {
        Node* node = new Node(data);
        if (!head) {
            head = tail = node;
        }
        else {
            head->prev = node; // link current head backward to the new node
            node->next = head; // link the new node forward to the current tail
            head = node; // update the new head
        }
    }
    
    void deleteNode(int data) {
        if (!head) {
            return;
        }
        
        Node* curr = head;
        while (curr) {
            if (curr->value == data) {
                // if the node is the current head (i.e. prev is a nullptr)
                if (!curr->prev) {
                    head = curr->next;
                }
                // otherwise, relink the previous node to the node after curr
                else {
                    curr->prev->next = curr->next;
                }
                
                // if the node is the current head (i.e. prev is a nullptr)
                if (!curr->next) {
                    tail = curr->prev;
                }
                // otherwise, relink the node after curr to the previous node
                else {
                    curr->next->prev = curr->prev;
                }
                delete curr;
                return;
            }
            curr = curr->next;
        }
    }
    
    // print list forward: head --> tail
    void printForward() {
        if (!head) { 
            cout << "Empty List!" << endl; 
            return; 
        }
        Node* curr = head;
        while (curr->next) {
            cout << curr->value << " <--> ";
            curr = curr->next;
        }
        cout << curr->value << endl;
    }

    // print list backward: tail --> head (replaces reverse())
    void printBackward() {
        if (!tail) { 
            cout << "Empty List!" << endl; 
            return; 
        }
        Node* curr = tail;
        while (curr->prev) {
            cout << curr->value << " <--> ";
            curr = curr->prev;
        }
        cout << curr->value << endl;
    }
};

int main() {
    DoublyLinkedList list;
    list.append(202);
    list.append(303);
    list.append(404);
    list.printForward();  // expect: 202 <--> 303 <--> 404

    list.addFront(101);
    list.deleteNode(404);
    list.printForward();  // expect: 101 <--> 202 <--> 303

    list.printBackward(); // expect: 303 <--> 202 <--> 101

    return 0;
}