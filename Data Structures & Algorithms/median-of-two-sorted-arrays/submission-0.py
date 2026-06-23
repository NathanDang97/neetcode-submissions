class Solution:
    # two-pointer solution, O(n + m) time, O(1) space
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        i1, i2 = 0, 0
        median1, median2 = 0, 0

        for _ in range((n + m) // 2 + 1):
            # track the last two picked median values
            # pivot median2 and update median1 with the smaller value between the two arrays
            median2 = median1 
            if i1 < n and i2 < m:
                if nums1[i1] < nums2[i2]:
                    median1 = nums1[i1]
                    i1 += 1
                else:
                    median1 = nums2[i2]
                    i2 += 1

            elif i1 < n:
                median1 = nums1[i1]
                i1 += 1
            else:
                median1 = nums2[i2]
                i2 += 1

        if (n + m) % 2 == 1:
            return float(median1)
        else:
            return float(median1 + median2) / 2.0
