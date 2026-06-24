# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # reverse and then merge solution, O(n) time, O(1) space
    # pass 1: find the middle of the list
    # pass 2: reverse the second half of the list
    # pass 3: merge the first half and the reversed second half
    def reorderList(self, head: Optional[ListNode]) -> None:
        # pass 1: find the middle part of the list (the slow pointer)
        # once fast reaches the end, slow will point to the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # pass 2: reverse the second half of the list
        middle_curr = slow.next # starting point of the half
        slow.next = None # disconnect the two halves before the merge
        prev = None # this will be the head of the reversed half
        while middle_curr:
            next = middle_curr.next
            middle_curr.next = prev
            prev = middle_curr
            middle_curr = next

        # pass 3: merge the two halves
        first_curr, second_curr = head, prev
        while second_curr:
            first_next, second_next = first_curr.next, second_curr.next
            first_curr.next = second_curr
            second_curr.next = first_next
            first_curr, second_curr = first_next, second_next
        