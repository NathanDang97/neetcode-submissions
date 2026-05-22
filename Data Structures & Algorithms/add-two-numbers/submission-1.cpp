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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* sum_list = new ListNode(); // this is a dummy node
        ListNode* curr_sum = sum_list;
        ListNode* curr1 = l1;
        ListNode* curr2 = l2;
        int carry = 0;

        while (curr1 || curr2 || carry != 0) {
            int val1 = (curr1) ? curr1->val : 0;
            int val2 = (curr2) ? curr2->val : 0;

            // add the current digits
            int sum_val = val1 + val2 + carry;
            carry = sum_val / 10;
            sum_val = sum_val % 10;
            curr_sum->next = new ListNode(sum_val);

            // adjust the pointers
            curr1 = (curr1) ? curr1->next : nullptr;
            curr2 = (curr2) ? curr2->next : nullptr;
            curr_sum = curr_sum->next;
        }

        ListNode* result = sum_list->next;
        delete sum_list;
        return result;
    }
};
