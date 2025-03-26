class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        for row in grid:
            for ele in row:
                nums.append(ele)

        nums.sort()

        median = nums[len(nums) // 2]

        operations = 0
        for num in nums:
            if num % x != median % x:
                return -1
            operations += abs(median - num) // x
        return operations