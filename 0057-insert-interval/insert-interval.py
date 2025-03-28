class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        idx = 0
        
        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            out.append(intervals[idx])
            idx += 1

        while idx < len(intervals) and intervals[idx][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[idx][0])
            newInterval[1] = max(newInterval[1], intervals[idx][1])
            idx += 1
        out.append(newInterval)
            
        while idx < len(intervals):
            out.append(intervals[idx])
            idx += 1
    
        return out
         