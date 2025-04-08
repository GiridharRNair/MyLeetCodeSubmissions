class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def check_unique(start):
            seen = set()
            for num in nums[start:]:
                if num in seen:
                    return False
                seen.add(num)
            return True

        count = 0
        for i in range(0, len(nums), 3):
            if check_unique(i):
                return count
            count += 1
        return count




            