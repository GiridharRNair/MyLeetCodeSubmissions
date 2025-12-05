class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n - 1

        for i in range(n - 1, -1, -1):
            jump_length = nums[i]

            if (i + jump_length) >= target:
                print(i, jump_length)
                target = i
        print(i)
        return target == 0