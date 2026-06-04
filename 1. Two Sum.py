class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Prevhash = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in Prevhash:
                return [Prevhash[diff], i]
            Prevhash[num] = i
