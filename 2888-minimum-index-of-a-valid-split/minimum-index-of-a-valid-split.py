class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        majority_num_count = 0
        majority_num = None

        count = 0
        for num in nums:
            if count == 0:
                majority_num = num
                count += 1
            elif majority_num == num:
                count += 1
            else:
                count -= 1
        
        for num in nums:
            if num == majority_num:
                majority_num_count += 1

        count = 0
        arr_len = len(nums)
        for idx in range(arr_len):
            if nums[idx] == majority_num:
                count += 1
            remaining_count = majority_num_count - count

            if (
                (count * 2) > idx + 1 and 
                (remaining_count * 2) > (arr_len - idx - 1)
            ):
                return idx


        return -1

            