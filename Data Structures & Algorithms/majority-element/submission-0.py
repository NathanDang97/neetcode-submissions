class Solution:
    # Boyter-Moore Voting algorithm, O(n) time, O(1) space
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = -1, 0
        for num in nums:
            if count == 0:
                candidate = num
            count = count + 1 if num == candidate else count - 1
        return candidate