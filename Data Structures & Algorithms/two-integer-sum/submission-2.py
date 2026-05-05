class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        residue = defaultdict(int)
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in residue:
                residue[num] = i
            else:
                return [residue[diff], i]

        return [None, None]
        
        