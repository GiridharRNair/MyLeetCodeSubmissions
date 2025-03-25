from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n_count = Counter(nums)
        for n in n_count:
            if n_count[n] > 1:
                return True
        return False