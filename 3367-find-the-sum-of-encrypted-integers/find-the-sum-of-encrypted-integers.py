class Solution:
    def encrypt(self, num):
        str_num = str(num)
        return int(max(str_num) * len(str_num))

    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        return sum([self.encrypt(x) for x in nums])