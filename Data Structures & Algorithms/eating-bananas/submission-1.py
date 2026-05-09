class Solution:
    # binary search solution, time O(nlogm)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = 0
        l, r = 1, max(piles)

        while l <= r:
            total_time = 0
            k = l + (r - l) // 2

            for pile in piles:
                total_time += math.ceil(pile / k)

            if total_time <= h:
                result = k
                r = k - 1
            else:
                l = k + 1

        return result