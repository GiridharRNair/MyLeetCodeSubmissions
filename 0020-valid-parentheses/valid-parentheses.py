class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []
        for p in s:
            if stack and p in p_map and p_map[p] == stack[-1]:
                stack.pop()
            else:
                stack.append(p)
        #     print(stack)
        # print(stack)
        return len(stack) == 0

        