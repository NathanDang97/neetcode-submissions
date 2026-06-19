# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # basic two-pointer solution, O(n + m) time, O(1) space
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        curr_merged = dummy_head
        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val > curr2.val:
                curr_merged.next = curr2
                curr2 = curr2.next
            else:
                curr_merged.next = curr1
                curr1 = curr1.next
            curr_merged = curr_merged.next

        curr_merged.next = curr1 if curr1 else curr2
        merged_head = dummy_head.next
        return merged_head