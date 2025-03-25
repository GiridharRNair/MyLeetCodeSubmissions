from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        s_counter = Counter(s)
        # print(s_counter)
        has_odd_freq = False
        for key in s_counter:
            if s_counter[key] % 2 == 0:
                count += s_counter[key]
            else:
                has_odd_freq = True
                count += s_counter[key] - 1
        
        if has_odd_freq:
            return count + 1
        return count
