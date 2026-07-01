class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
         
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            m = l + (r-l)//2

            t_hour = 0

            for b in piles:
                t_hour += math.ceil(b/m)
                
            if t_hour > h:
                l = m + 1
            else:
                res = m
                r = m - 1
        return res


        

        