class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()

        computer_batteries = batteries[-n:]
        extra = sum(batteries[:-n])
        # print(extra // 0)
        # [7, 5, 10, 12]
        # [5, 10, 12]
        # [10, 10, 12]

        for i in range(n - 1):
            battery_difference = computer_batteries[i + 1] - computer_batteries[i]
            if battery_difference <= (extra // (i + 1)):
                extra -= battery_difference * (i + 1)
            else:
                return computer_batteries[i] + (extra // (i + 1))

        return computer_batteries[-1] + (extra // n)