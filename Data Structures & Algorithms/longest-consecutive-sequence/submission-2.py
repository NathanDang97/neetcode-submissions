class Solution:
    # O(n) solution
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums_set = set(nums)

        for num in nums:
            # begin a new sequence with num
            if (num - 1) not in nums_set:
                curr_length = 1

                # compute the length of the sequence
                while (num + curr_length) in nums_set:
                    curr_length += 1
            
                # update the max length
                result = max(result, curr_length)

        return result

