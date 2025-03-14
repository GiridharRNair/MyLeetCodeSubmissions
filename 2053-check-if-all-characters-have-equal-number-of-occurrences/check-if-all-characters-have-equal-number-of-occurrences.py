class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        set_s = set(s)
        count = s.count(s[0])
        for c in set_s:
            if s.count(c) != count:
                return False
        return True
        