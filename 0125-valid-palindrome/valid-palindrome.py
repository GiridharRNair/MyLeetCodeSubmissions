class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if c.isdigit() or c.isalnum():
                new_s += c
        return new_s.lower() == new_s.lower()[::-1]