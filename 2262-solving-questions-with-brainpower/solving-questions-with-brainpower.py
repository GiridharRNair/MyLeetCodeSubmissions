class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * 1000001
        for i in range(len(questions) - 1, -1, -1):
            points = questions[i][0]
            brainpower = questions[i][1]
            dp[i] = max(
                points + dp[min(brainpower + i + 1, len(questions))],
                dp[i + 1]
            )
        return dp[0]