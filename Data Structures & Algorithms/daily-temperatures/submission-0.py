class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        n = len(temperatures)
        
        for i in range(n):
            for j in range(i,n):
                if temperatures[i] <  temperatures[j]:
                    res.append(j-i)
                    break
                elif j >= n-1:
                    res.append(0)

        return res
             