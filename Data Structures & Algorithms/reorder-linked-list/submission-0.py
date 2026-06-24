# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # 2-pass brute-force solution, O(n) time and space
    # pass 1: convert the list to an array and pass 2: use two-pointer
    def reorderList(self, head: Optional[ListNode]) -> None:
        # pass 1
        arr_list = []
        curr = head
        while (curr):
            arr_list.append(curr)
            curr = curr.next

        # pass 2
        l, r = 0, len(arr_list) - 1
        while l < r:
            arr_list[l].next = arr_list[r]
            l += 1
            if l >= r:
                break
            arr_list[r].next = arr_list[l]
            r -= 1
        arr_list[l].next = None