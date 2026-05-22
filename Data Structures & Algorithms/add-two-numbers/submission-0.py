# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_list = ListNode() # this is a dummy node
        curr_sum = sum_list
        curr1, curr2 = l1, l2
        carry = 0

        while curr1 or curr2 or carry:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0

            # add the current digits
            sum_val = val1 + val2 + carry
            carry = sum_val // 10 # the whole part
            sum_val = sum_val % 10 # remainder
            curr_sum.next = ListNode(sum_val)

            # move the pointers
            curr_sum = curr_sum.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None

        return sum_list.next

