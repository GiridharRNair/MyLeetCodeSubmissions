class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if ":" in queryIP:
            return self.validateIPV6(queryIP)
        elif "." in queryIP:
            return self.validateIPV4(queryIP)
        else:
            return "Neither"

    def validateIPV4(self, queryIP):
        nums = queryIP.split(".")
        if len(nums) != 4:
            return "Neither"
        for num in nums:


            if not num:
                return "Neither"
            if len(num) > 1 and num[0] == "0":
                return "Neither"
            if any(c.isalpha() for c in num):
                return "Neither"
            if not (0 <= int(num) <= 255):
                return "Neither"
        return "IPv4"


    def validateIPV6(self, queryIP):
        valid_hex_chars = "0123456789abcdefABCDEF"
        things = queryIP.split(":")
        if len(things) != 8:
            return "Neither"
        for thing in things:
            if not thing:
                return "Neither"
            if len(thing) > 4:
                return "Neither"
            if not all(c in valid_hex_chars for c in thing):
                return "Neither"
        return "IPv6"