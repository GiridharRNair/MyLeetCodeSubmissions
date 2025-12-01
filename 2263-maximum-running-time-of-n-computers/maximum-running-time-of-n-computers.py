class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()

        extra = sum(batteries[:-n])

        computer_batteries = batteries[-n:]

        for i in range(n - 1):
            if computer_batteries[i + 1] - computer_batteries[i] <= extra // (i + 1):
                extra -= (computer_batteries[i + 1] - computer_batteries[i]) * (i + 1)
            else:
                return computer_batteries[i] + extra // (i + 1)

        return computer_batteries[-1] + extra // n

