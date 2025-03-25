class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = 0
        max_sub = float("-inf")
        for num in nums:
            prefix_sum += num
            max_sub = max(prefix_sum, max_sub)
            if prefix_sum < 0:
                prefix_sum = 0
        return max_sub