class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def backtrack(options, perm):
            if not options:
                permutations.append(perm[:])
                return 

            for i in range(len(options)):
                # add the current option to the permutation
                perm.append(options[i])
                # remove the chosen element from the available options
                backtrack(options[:i] + options[i+1:], perm)
                # reset the state of the permutation to try other options
                perm.pop()

        backtrack(nums, [])
        return permutations