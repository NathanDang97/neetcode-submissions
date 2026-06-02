class Solution:
    # hash-map & prefix-sum solution, O(n) time, O(n) space
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        # maps a prefix sum to its frequency
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1 # there is one empty prefix sum

        curr_sum = 0
        for i in range(len(nums)):
            # compute the prefix sum up to index i
            curr_sum += nums[i]

            # check if a prefix sum of (curr_sum - k) already presents
            diff = curr_sum - k
            count += prefix_sums[diff]

            # increase the frequency of the current prefix sum
            prefix_sums[curr_sum] += 1

        return count 