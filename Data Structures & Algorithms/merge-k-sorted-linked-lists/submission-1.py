# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # divide and conquer solution, O(n * logk) time, O(k) space 
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # helper method to merge 2 sorted lists
        def merge2Lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy_merged_head = ListNode(0)
            curr = dummy_merged_head

            while l1 and l2:
                if l1.val > l2.val:
                    curr.next = l2
                    l2 = l2.next
                else:
                    curr.next = l1
                    l1 = l1.next

                curr = curr.next

            if l1:
                curr.next = l1
            if l2:
                curr.next = l2

            merged_head = dummy_merged_head.next
            return merged_head

        if not lists:
            return None
        
        # treat this similarly to merge sort
        # pair up two lists to merge them and repeat until we have one final list
        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_l = merge2Lists(l1, l2)
                merged_lists.append(merged_l)
            
            # update the current list of lists
            lists = merged_lists

        # note that lists now should only contain one final sorted list
        return lists[0]
        