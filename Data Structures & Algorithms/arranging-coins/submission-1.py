class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        temp = n
        for i in range(1,n+1):
            temp -= i
            if temp < 0:
                return res
            else:
                res += 1
        return res