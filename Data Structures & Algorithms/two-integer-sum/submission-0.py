class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2idx = {}
        for i, n in enumerate(nums):
            other = target - n
            if other in num2idx:
                return [num2idx[other], i]
            else:
                num2idx[n] = i
        return []
