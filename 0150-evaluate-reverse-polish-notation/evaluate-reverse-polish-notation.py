class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        out = 0
        nums = []
        for token in tokens:
            if token == "+":
                a, b = nums.pop(), nums.pop()
                nums.append(int(a + b))
            elif token == "-":
                a, b = nums.pop(), nums.pop()
                nums.append(int(b - a))
            elif token == "*":
                a, b = nums.pop(), nums.pop()
                nums.append(int(b * a))
            elif token == "/":
                a, b = nums.pop(), nums.pop()
                nums.append(int(b / a))
            else:
                nums.append(int(token))
        return nums[-1]

        