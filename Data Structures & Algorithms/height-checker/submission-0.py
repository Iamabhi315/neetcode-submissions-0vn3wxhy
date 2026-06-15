class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        count = 0

        temp = sorted(heights)

        for i in range(n):
            if heights[i] != temp[i]:
                count += 1
        
        return count