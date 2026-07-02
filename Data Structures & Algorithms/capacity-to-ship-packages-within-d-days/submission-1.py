class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        capacity = r

        while l <= r:
            m = l + (r - l) // 2

            d = 0
            s = 0

            for w in weights:
                s += w

                if s == m:
                    d += 1
                    s = 0

                elif s > m:
                    d += 1
                    s = w

            if s > 0:      # last day
                d += 1

            if d > days:
                l = m + 1
            else:
                capacity = m
                r = m - 1

        return capacity