class Solution:
    def arrangeCoins(self, n: int):
        low, high = 0, n

        while low <= high:
            mid = (low + high) // 2
            coins = mid * (mid + 1) // 2

            if coins == n:
                return mid
            elif coins < n:
                low = mid + 1
            else:
                high = mid - 1

        return high