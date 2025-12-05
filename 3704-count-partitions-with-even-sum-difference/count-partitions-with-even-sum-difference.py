class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)

        prefix_sums = [0] * n
        suffix_sums = [0] * n

        for i in range(1, n):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]
            

        for i in range(n - 2, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + nums[i + 1]

        print(prefix_sums)
        print(suffix_sums)

        res = 0
        for i in range(1, n):
            if (suffix_sums[i - 1] + prefix_sums[i]) % 2 == 0:
                res += 1
        
        return res
