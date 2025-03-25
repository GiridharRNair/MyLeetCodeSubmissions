from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n_count = Counter(nums)
        return max(n_count, key = lambda x:n_count[x])
