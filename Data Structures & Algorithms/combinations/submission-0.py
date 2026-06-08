class Solution:
    # backtracking solution, O(k * (n choose k)) time and space
    def combine(self, n: int, k: int) -> List[List[int]]:
        all_combinations = []

        def backtrack(start, combination):
            if len(combination) == k:
                all_combinations.append(combination[:])
                return 

            for i in range(start, n + 1):
                combination.append(i)
                backtrack(i + 1, combination)
                combination.pop()

        backtrack(1, [])
        return all_combinations