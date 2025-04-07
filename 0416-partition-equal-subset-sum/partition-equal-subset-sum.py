class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_n = sum(nums)
        target_sum = sum_n // 2
        if sum_n % 2 != 0:
            return False
        
        dp = [False] * (target_sum + 1)
        dp[0] = True

        for num in nums:
            for curr_sum in range(target_sum, num - 1, -1):
                dp[curr_sum] = dp[curr_sum] or dp[curr_sum - num]
            # print(dp)
        return dp[target_sum]
        


