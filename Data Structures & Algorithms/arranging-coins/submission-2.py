class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        i = 1
        temp = n
        while temp > 0:
            temp -= (res+1)
            if temp < 0:
                return res
            res += 1
        return res