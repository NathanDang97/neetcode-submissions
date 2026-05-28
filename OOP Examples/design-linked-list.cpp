#include <iostream>
using namespace std;
    
struct Node {
    int value; // node data
    Node* next; // pointer to the next node
    Node(int x): value(x), next(nullptr) {}
};

class LinkedList {
private:
    Node* head; // pointer to the first node
public:
    // constructor: initialize to an empty list
    LinkedList(): head(nullptr) {}
    
    // destructor: remove all created nodes to deallocate memory
    // Note: "curr" stands for current
    ~LinkedList() {
        Node* curr = head;  // Start with the head node
        while (curr != nullptr) {  // Iterate until the end of the list
            Node* nextNode = curr->next;  // Store the next node
            delete curr;  // Delete the current node
            curr = nextNode;  // Move to the next node
        }
    }
    
    // add a node to the end of the list, O(n) time
    void append(int data) {
        Node* node = new Node(data); // create new node
        // if the list is empty, then the new node is the head
        if (!head) {
            head = node;
        }
        // otherwise, traverse to the end of the list and add the new node
        else {
            Node* curr = head;
            while (curr->next) {
                curr = curr->next;
            }
            curr->next = node;
        }
    } 
    
    // add a node to the beginning of the list, O(1) time
    void addFirst(int data) {
        Node* node = new Node(data); // create new node

        if (head != nullptr) {
            node->next = head; // link new node to the current head
        }
        head = node; // update head to new node
    }
    
    // remove a node with a given data value
    void deleteNode(int data) {
        if (!head) {
            return;
        }
        
        // if the node to be deleted is the head node
        if (head->value == data) {
            Node* temp = head;
            head = head->next;
            delete temp;
            return;
        }
        
        // otherwise, traverse to one position before the node to be deleted,
        // then unlink and remove this node from the list
        Node* curr = head;
        while (curr->next) {
            if (curr->next->value == data) {
                Node* temp = curr->next;
                curr->next = curr->next->next;
                delete temp;
                return;
            }
            curr = curr->next;
        }
    }
    
    void reverse() {
        Node* prev = nullptr;
        Node* curr = head;
        
        while (curr) {
            // reverse the link
            Node* next = curr->next;
            curr->next = prev;
            // proceed to the next node
            prev = curr;
            curr = next;
        }
        head = prev;
        return;
    }
    
    void printList() {
        if (!head) { 
            cout << "Empty List!" << endl; 
            return; 
        }
        Node* curr = head;
        while (curr->next) {
            cout << curr->value << " ---> ";
            curr = curr->next;
        }
        cout << curr->value;
        cout << endl;
    }
};

int main() {
    LinkedList list;
    list.append(202);
    list.append(303);
    list.append(404);
    list.printList(); // expect: 202 ---> 303 ---> 404
    
    list.addFirst(101);
    list.deleteNode(404);
    list.printList(); // expect: 101 ---> 202 ---> 303
    
    list.reverse();
    list.printList(); // expect: 303 ---> 202 ---> 101
        
    return 0;
}