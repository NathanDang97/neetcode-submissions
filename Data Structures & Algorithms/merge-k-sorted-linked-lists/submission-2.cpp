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
    // solution using min-heap, O(nlogk) time, O(k) space
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) {
            return nullptr;
        }

        // the min-heap stores the each current min element of the k lists
        auto comparator = [](ListNode* a, ListNode* b) {
            return a->val > b->val;
        };
        priority_queue<ListNode*, vector<ListNode*>, decltype(comparator)> minHeap(comparator);
        for (ListNode* list : lists) {
            if (list != nullptr){
                minHeap.push(list);
            }
        }

        ListNode* merged = new ListNode(0);
        ListNode* curr = merged;
        while (!minHeap.empty()) {
            ListNode* curr_min_node = minHeap.top();
            minHeap.pop();
            curr->next = curr_min_node;
            curr = curr->next;

            // if the list where the min node was taken from still has more node(s)
            // add the next one to the queue
            curr_min_node = curr_min_node->next;
            if (curr_min_node != nullptr) {
                minHeap.push(curr_min_node);
            }
        }
        
        return merged->next;
    }
};
