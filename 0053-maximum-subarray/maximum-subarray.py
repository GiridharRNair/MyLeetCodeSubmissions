class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # prefix_sums = 0
        # max_sum = float("-inf")
        # for num in nums:
        #     prefix_sums += num
        #     max_sum = max(prefix_sums, max_sum)
        #     if prefix_sums < 0:
        #         prefix_sums = 0
        # return max_sum
        def crossing_sum(arr, left, right, middle):
            left_sum = 0
            left_max_sum = float("-inf")
            for idx in range(middle, left - 1, -1):
                left_sum += arr[idx]
                left_max_sum = max(left_max_sum, left_sum)

            right_sum = 0
            right_max_sum = float("-inf")
            for idx in range(middle + 1, right + 1):
                right_sum += arr[idx]
                right_max_sum = max(right_max_sum, right_sum)

            return max(
                left_max_sum,
                right_max_sum,
                right_max_sum + left_max_sum
            )


        
        def dc(arr, left, right):
            if left > right:
                return float("-inf")
            if left == right: # one element
                return arr[left]
            
            middle = (left + right) // 2

            return max(
                dc(arr, left, middle),
                dc(arr, middle + 1, right),
                crossing_sum(arr, left, right, middle)
            )


        return dc(nums, 0, len(nums) - 1)