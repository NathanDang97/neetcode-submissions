class Solution:
    # monotonic stack solution, O(n + m) time, O(m) space
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_idx_map = {num : i for i, num in enumerate(nums1)}
        result = [-1] * len(nums1)
        stack = [] # the monotonic stack

        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = nums1_idx_map[val]
                result[idx] = curr

            if curr in nums1_idx_map:
                stack.append(curr)

        return result