#include <iostream>
#include <unordered_set>
#include <unordered_map>
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
        
        // order of operations matters: unlink must be done before deleting the node
        Node* curr = head;
        Node* prev = nullptr;
        while (curr) {
            if (curr->value == data) {
                Node* temp = curr;
                if (!prev) {
                    head = curr->next;
                }
                else {
                    prev->next = curr->next;
                }
                curr = curr->next;
                delete temp;
                return;
            }
            else {
                prev = curr;
                curr = curr->next;
            }
        }
    }
    
    // delete a node from a given nth-index from the end of the list (1-indexed)
    void deleteNthNodeFromEnd(int n) {
        // compute the length of the list
        int length = 0;
        Node* curr = head;
        while (curr) {
            length++;
            curr = curr->next;
        }
        
        int removeIndex = length - n;
        curr = head;
        Node* prev = nullptr;
        // if the node to be removed is the head
        if (removeIndex == 0) {
            head = curr->next;
            delete curr;
            return;
        }
        
        for (int i = 0; i < length - 1; i++) {
            if (i == removeIndex - 1) {
                Node* temp = curr;
                prev->next = curr->next;
                curr = curr->next;
                delete temp;
                return;
            }
            else {
                prev = curr;
                curr = curr->next;
            }
        }
    } 
    
    // remove duplicates from the end of the list
    void removeDuplicatesFromEnd() {
        unordered_set<int> seen;
        Node* curr = head;
        Node* prev = nullptr;
        while (curr) {
            if (seen.find(curr->value) != seen.end()) {
                prev->next = curr->next;
                delete curr;
                curr = prev->next;
            }
            else {
                seen.insert(curr->value);
                prev = curr;
                curr = curr->next;
            }
        }
    }
    
    // remove duplicates from the beginning of the list
    void removeDuplicatesFromBeginning() {
        // first pass: count the frequency of each element
        unordered_map<int, int> frequency;
        Node* curr = head;
        while (curr) {
            frequency[curr->value]++;
            curr = curr->next;
        }
        
        // second pass: skip nodes that are not the last occurrence
        // by removing the node if its remaining count is still > 0
        curr = head;
        Node* prev = nullptr;
        while (curr) {
            frequency[curr->value]--;
            if (frequency[curr->value] > 0) {
                Node* temp = curr;
                if (!prev) {
                    head = curr->next;
                }
                else {
                    prev->next = curr->next;
                }
                curr = curr->next;
                delete temp;
            }
            else {
                prev = curr;
                curr = curr->next;
            }
        }
    }
    
    // reverse the entire list
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
    
    // reverse a sublist defined by the given start and end indices (1-indexed)
    void reverseBetween(int start, int end) {
        // create a dummy node for the edge case when left = 1
        // in this case, the head of the list changes after reversal
        Node* dummy = new Node(0);
        dummy->next = head;
        Node* prev = dummy;
        
        // find the start position
        for (int i = 0; i < start - 1; i++) {
            prev = prev->next;
        }
        Node* sublistHead = prev->next;
        Node* sublistTail = sublistHead;
        
        // find the end position
        for (int i = 0; i < end - start; i++) {
            sublistTail = sublistTail->next;
        }
        
        // detache the sublist that we need to reverse
        Node* nextNode = sublistTail->next;
        sublistTail->next = nullptr;
        
        // reverse the sublist
        Node* subPrev = nullptr;
        Node* subCurr = sublistHead;
        Node* originalTail = sublistHead; // save tail before overwriting sublistHead
        while (subCurr) {
            Node* next = subCurr->next;
            subCurr->next = subPrev;
            subPrev = subCurr;
            subCurr = next;
        }
        sublistHead = subPrev;

        // re-attach the reversed sublist
        prev->next = sublistHead;
        originalTail->next = nextNode; // use saved tail, not sublistHead
        
        // clean up the dummy node
        head = dummy->next;
        delete dummy;
    }
    
    // display the current linked list
    void printList() {
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
    
    list.append(404);
    list.append(202);
    list.append(303);
    list.removeDuplicatesFromEnd();
    list.printList(); // expect: 303 ---> 202 ---> 101 ---> 404
    
    list.addFirst(404);
    list.append(202);
    list.removeDuplicatesFromBeginning();
    list.printList(); // expect: 303 ---> 101 ---> 404 ---> 202
    
    list.addFirst(505);
    list.append(505);
    list.append(505);
    list.deleteNthNodeFromEnd(7);
    list.deleteNthNodeFromEnd(1);
    list.printList(); // expect: 303 ---> 101 ---> 404 ---> 202 ---> 505
    
    list.reverseBetween(1, 2); // expect: 101 ---> 303 ---> 404 ---> 202 ---> 505
    list.printList();
    list.reverseBetween(3, 4); // expect: 101 ---> 303 ---> 202 ---> 404 ---> 505
    list.printList();
    list.reverseBetween(2, 3); // expect: 101 ---> 202 ---> 303 ---> 404 ---> 505
    list.printList();
        
    return 0;
}