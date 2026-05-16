class Solution:
    # bucket sort solution, O(n) time
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # buckets[i] is the numbers that appear i times
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in frequency.items():
            buckets[freq].append(num)

        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result