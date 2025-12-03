class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        y_cord_store = defaultdict(int)
        res = 0
        total_sum = 0
        MOD = 10 ** 9 + 7

        for x, y in points:
            y_cord_store[y] += 1

        for y_count in y_cord_store.values():
            unique_trapazoids = (y_count * (y_count - 1)) // 2
            # print((y_count * (y_count - 1)) // 3, unique_trapazoids)
            res += (unique_trapazoids * total_sum)
            total_sum += unique_trapazoids
        return res % MOD