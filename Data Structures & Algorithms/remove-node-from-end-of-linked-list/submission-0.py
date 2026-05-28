# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # compute the length of the list
        list_length = 0
        curr = head
        while curr:
            list_length += 1
            curr = curr.next

        # compute the position of the node to be remove starting from the beginning
        stop = list_length - n
        if stop == 0:
            return head.next

        curr = head
        for i in range(list_length - 1):
            # disconnect the node from the list
            if i == (stop - 1):
                curr.next = curr.next.next
                break
            curr = curr.next

        return head
