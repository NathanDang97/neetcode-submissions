# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # create a dummy node for the edge case of when left = 1
        # in this case, the head of the list changes after reversal
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # helper method to reverse a given list
        def reverse(head):
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        # find the starting position
        for _ in range(left - 1):
            prev = prev.next

        sublist_head = prev.next
        sublist_tail = sublist_head
        # find the ending position
        for _ in range(right - left):
            sublist_tail = sublist_tail.next

        # detach the sublist that we need to reverse
        next_node = sublist_tail.next # the head of the reversed sublist will attach to this node
        sublist_tail.next = None

        # reverse the sublist
        reversed_sublist = reverse(sublist_head)
        
        # reconnect the reversed sublist back to the original list
        prev.next = reversed_sublist
        sublist_head.next = next_node

        return dummy.next


        