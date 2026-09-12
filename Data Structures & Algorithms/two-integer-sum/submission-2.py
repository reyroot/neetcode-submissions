class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):            
            seen[n] = i

        for i, n in enumerate(nums):
            r = target - n
            if r in seen and seen[r] != i:
                return [i, seen[r]]
