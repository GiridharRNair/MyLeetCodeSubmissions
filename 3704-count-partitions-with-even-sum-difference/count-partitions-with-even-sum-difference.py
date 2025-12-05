class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sums = [0] * n

        prefix_sums[0] = nums[0]
        for i in range(1, n):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i]

        total_sum = prefix_sums[-1]
        # print(prefix_sums)
        res = 0
        for i in range(n - 1):
            prefix_sum = prefix_sums[i]
            
            if (prefix_sum - (total_sum - prefix_sum)) % 2 == 0:
                # print(total_sum, prefix_sum)
                res += 1
        
        return res