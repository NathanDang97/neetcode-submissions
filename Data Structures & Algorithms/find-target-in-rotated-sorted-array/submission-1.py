class Solution:
    # binary search solution (3 passes), O(log n) time
    def search(self, nums: List[int], target: int) -> int:

        # pass 1: find the pivot (the rotated point)
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l
        
        def binary_search(left : int, right : int) -> int:
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return - 1 

        # pass 2: search the left half
        result = binary_search(0, pivot - 1)
        if result != -1:
            return result

        # pass 3: search the right half if the previous search fails
        return binary_search(pivot, len(nums) - 1)