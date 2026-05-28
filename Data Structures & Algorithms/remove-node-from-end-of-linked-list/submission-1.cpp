/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    // two-pass solution, O(n) time, O(1) space
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int length = 0;
        ListNode* curr = head;
        while (curr) {
            length++;
            curr = curr->next;
        }

        int removeIndex = length - n;
        // if the node needs to be removed is the head
        if (removeIndex == 0) {
            ListNode* temp = head;
            head = head->next;
            delete temp;
            return head;
        }

        curr = head;
        for (int i = 0; i < length - 1; i++) {
            if (i == removeIndex - 1) {
                ListNode* temp = curr->next;
                curr->next = curr->next->next;
                delete temp;
                break;
            }
            curr = curr->next;
        }
        return head;
    }
};
