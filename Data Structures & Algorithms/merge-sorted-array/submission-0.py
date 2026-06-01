class Solution:
    # two-pointer solution, O(n) time
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_idx = m + n - 1
        i, j = m - 1, n - 1

        # merge in reversed order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last_idx] = nums1[i]
                i -= 1
            else:
                nums1[last_idx] = nums2[j]
                j -= 1
            last_idx -= 1

        # fill the leftover of nums2 to nums1 if any
        while j >= 0:
            nums1[last_idx] = nums2[j]
            j -= 1
            last_idx -= 1