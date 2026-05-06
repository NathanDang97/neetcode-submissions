class Solution:
    # O(n^2) brute-force solution
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            curr_length = 1

            while (num + curr_length) in nums:
                curr_length += 1
            
            result = max(result, curr_length)

        return result

