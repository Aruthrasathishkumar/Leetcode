# Leetcode 152
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        CurMax, CurMin = 1, 1

        for n in nums:
            temp = CurMax
            
            CurMax = max(n * CurMax, n * CurMin, n)
            CurMin = min(n * temp, n * CurMin, n)
            res = max(res, CurMax)
        return res
