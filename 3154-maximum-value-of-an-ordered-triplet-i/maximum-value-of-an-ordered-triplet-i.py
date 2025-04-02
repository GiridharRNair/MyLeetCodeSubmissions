class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        left_max = [0] * len(nums)
        for i in range(1, len(nums)):
            left_max[i] = max(left_max[i - 1], nums[i - 1])

        right_max = [0] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i + 1])
        out = float("-inf")
        for idx, num in enumerate(nums):
            out = max(out, (left_max[idx] - num) * right_max[idx])
        return out