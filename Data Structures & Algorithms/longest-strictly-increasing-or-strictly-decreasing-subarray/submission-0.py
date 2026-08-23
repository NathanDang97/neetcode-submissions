class Solution:
    # brute-force solution, O(n^2) time, O(1) space
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        longest = 1

        for i in range(n - 1):
            curr_streak = 1
            for j in range(i + 1, n):
                if nums[j] == nums[j - 1] or ((nums[i] < nums[i + 1]) != (nums[j - 1] < nums[j])):
                    break
                curr_streak += 1

            longest = max(longest, curr_streak)

        return longest