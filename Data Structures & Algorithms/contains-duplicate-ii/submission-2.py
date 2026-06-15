class Solution:
    # two-pointer solution, O(n) time, O(min(n, k)) space
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, 0
        window = set()

        while r < len(nums):
            # remove nums[l] from the set and increment l if the window's size exceeds k
            if r - l > k:
                window.remove(nums[l])
                l += 1
            
            # if nums[r] already in the set, return True since we always keep the set's size to <= k
            if nums[r] in window:
                return True

            # add nums[r] to the set
            window.add(nums[r])
            r += 1

        return False