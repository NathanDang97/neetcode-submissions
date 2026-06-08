class Solution:
    # backtracking solution, time O(2^{t/m}) and space O(t/m)
    # where t is the target and m is the smallest number in nums
    # this is because the same number nums[i] can be used multiple times
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        all_comb_sums = []
        nums.sort() # use sorting to optimize a little
                    # since once a number makes the sum exceed the target
                    # all numbers after it will also exceed the target
                    # so we can stop exploring further

        def backtrack(start, combination, curr_sum):
            if curr_sum == target:
                all_comb_sums.append(combination[:])
                return

            for i in range(start, len(nums)):
                if curr_sum + nums[i] > target:
                    return
                combination.append(nums[i])
                backtrack(i, combination, curr_sum + nums[i])
                combination.pop()

        backtrack(0, [], 0)
        return all_comb_sums