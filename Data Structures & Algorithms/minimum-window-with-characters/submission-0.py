class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dit = defaultdict(int)

        for c in t:
            dit[c] += 1

        required_count = len(t)
        l = 0

        window_size = float('inf')
        start_i = 0

        for r in range(len(s)):

            dit[s[r]] -= 1

            if s[r] in dit and dit[s[r]] >= 0:
                required_count -= 1

            while required_count == 0:

                if r - l + 1 < window_size:
                    window_size = r - l + 1
                    start_i = l

                dit[s[l]] += 1

                if dit[s[l]] > 0:
                    required_count += 1

                l += 1

        if window_size == float('inf'):
            return ""

        return s[start_i:start_i + window_size]