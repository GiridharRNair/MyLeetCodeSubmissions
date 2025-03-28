class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s):
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                string_1 = s[:left] + s[left + 1:]
                string_2 = s[:right] + s[right + 1:]
                return is_palindrome(string_1) or is_palindrome(string_2)
            left += 1
            right -= 1
        return True
            # aca
            # aba