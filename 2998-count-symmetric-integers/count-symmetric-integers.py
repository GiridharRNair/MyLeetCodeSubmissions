class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            num_str = str(num)
            length = len(num_str)
            if length % 2 == 1:
                continue
            
            left_sum = sum(int(num_str[i]) for i in range(length // 2))
            right_sum = sum(int(num_str[i]) for i in range(length // 2, length))

            if left_sum == right_sum:
                count += 1
        return count