class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        maxi = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[maxi] < dp[i]:
                maxi = i
        out = []
        while maxi >= 0:
            out.append(nums[maxi])
            maxi = prev[maxi]
        return out

        