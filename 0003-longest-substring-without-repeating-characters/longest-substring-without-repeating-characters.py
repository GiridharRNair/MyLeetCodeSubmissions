class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        left = 0
        right = 0
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                max_len = max(max_len, right - left)
            else:
                seen.remove(s[left])
                left += 1
        return max_len