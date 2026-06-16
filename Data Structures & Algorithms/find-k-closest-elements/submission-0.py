class Solution:
    # two-pointer solution, O(n - k) time, O(k) space
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # since the input array is sorted, k closest elements (to x) must form a contiguous subarray
        # use two pointers, one at each end of the array, and shrink the window by removing those further from x
        # stop the process until k elements remain
        l, r = 0, len(arr) - 1
        while r - l >= k:
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1
        
        return arr[l:r + 1]