class Solution:
    # suffix max solution, O(n) time, O(1) space
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [0] * len(arr)
        right_max = -1
        for i in range(len(arr) - 1, -1, -1):
            result[i] = right_max
            right_max = max(right_max, arr[i])
        return result