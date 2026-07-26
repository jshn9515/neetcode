from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        cnt = Counter(nums)
        result = cnt.most_common(k)
        result = [r[0] for r in result]
        return result
