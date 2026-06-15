class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = defaultdict(int)

        for ch in text:
            count[ch] += 1

        return min(
            count['b'],
            count['a'],
            count['l'] // 2,
            count['o'] // 2,
            count['n']
        )