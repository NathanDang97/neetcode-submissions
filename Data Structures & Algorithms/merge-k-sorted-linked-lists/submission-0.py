import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# a comparator/wrapper to compare the values of two nodes
# this will be useful for implementing a min heap
class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    # solution using a min-heap, time O(n * logk), space O(k)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        # create a dummy node to anchor the merged list
        # then later, the next node of this dummy node is the head of the merged list
        merged_list_dummy_node = ListNode(0)
        curr = merged_list_dummy_node
        # the min heap helps keep track of the minimum across all k values of the list heads
        min_heap = []
        for list_head in lists:
            if list_head is not None:
                heapq.heappush(min_heap, NodeWrapper(list_head))

        while min_heap:
            curr_node_wrapper = heapq.heappop(min_heap)
            curr.next = curr_node_wrapper.node
            curr = curr.next

            if curr_node_wrapper.node.next:
                heapq.heappush(min_heap, NodeWrapper(curr_node_wrapper.node.next))

        merged_list_head = merged_list_dummy_node.next
        return merged_list_head