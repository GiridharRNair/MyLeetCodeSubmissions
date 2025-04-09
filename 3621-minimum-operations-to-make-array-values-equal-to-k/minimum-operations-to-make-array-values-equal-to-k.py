class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        out = set()
        for x in nums:
            if x < k:
                return -1
            elif x > k:
                out.add(x)
        return len(out)