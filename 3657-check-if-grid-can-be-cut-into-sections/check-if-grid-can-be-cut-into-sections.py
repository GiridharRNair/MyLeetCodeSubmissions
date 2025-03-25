class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        sort_y = sorted(rectangles, key = lambda rect: rect[1])        
        sort_x = sorted(rectangles, key = lambda rect: rect[0])
        return self._check(sort_y, False) or self._check(sort_x, True)
    def _check (self, rectangles, vertical: bool):
        last_split_end = 0
        splits = 0
        if not vertical:
            for r in rectangles:
                if r[1] >= last_split_end:
                    splits += 1
                
                last_split_end = max(last_split_end, r[3])
        else:
            for r in rectangles:
                if r[0] >= last_split_end:
                    splits += 1
                
                last_split_end = max (last_split_end, r[2])
        return splits >= 3