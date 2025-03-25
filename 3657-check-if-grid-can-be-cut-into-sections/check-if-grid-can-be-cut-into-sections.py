class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        return self._check(rectangles, False) or self._check(rectangles, True)

    def _check (self, rectangles, vertical: bool):
        last_split_end = 0
        splits = 0
        if vertical: 
            idx = 0 
        else:
            idx = 1
        rectangles = sorted(rectangles, key = lambda rect: rect[idx])

        for r in rectangles:
            if r[idx] >= last_split_end:
                splits += 1
            
            last_split_end = max(last_split_end, r[idx+2])
            if splits >= 3:
                return True
        return False 