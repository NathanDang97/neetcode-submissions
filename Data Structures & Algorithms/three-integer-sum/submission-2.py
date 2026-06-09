class Solution:
    # sorting + two-pointer solution, O(n^2) time, O(1) or O(n) space depending on the sorting algorithm
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        all_triplets = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0:
                break # since all remaining sorted numbers are positive

            # skip duplicate values for the first number
            if i > 0 and n == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = n + nums[l] + nums[r]
                if curr_sum < 0:
                    l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    all_triplets.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip all duplicates to make sure the returned triplets are unique
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1

        return all_triplets