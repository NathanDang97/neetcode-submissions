class Solution:
    # brute-force solution, O(n) time
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1