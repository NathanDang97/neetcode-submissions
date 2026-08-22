class Solution:
    # brute-force solution, O(n * m) time, O(1) space
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range(len(nums1)):
            next_greater = -1
            for j in range(len(nums2) - 1, -1, -1):
                if nums2[j] > nums1[i]:
                    next_greater = nums2[j]
                elif nums2[j] == nums1[i]:
                    break
            result.append(next_greater)
        return result