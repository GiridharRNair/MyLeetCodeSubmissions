import heapq

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        chosen_queries = 0
        candidates = []
        chosen = []
        index = 0
        query_index = 0

        while index < len(nums):
            while query_index < len(queries) and index >= queries[query_index][0]:
                heapq.heappush(candidates, -queries[query_index][1])
                query_index += 1

            num = nums[index]

            while candidates and len(chosen) < num:
                end = abs(heapq.heappop(candidates))
                if end >= index:
                    heapq.heappush(chosen, end)
                    chosen_queries += 1

            if nums[index] > len(chosen):
                return -1

            nums[index] = 0

            while chosen and chosen[0] <= index:
                heapq.heappop(chosen)

            index += 1

        return len(queries) - chosen_queries

            

        print(heap_1)
