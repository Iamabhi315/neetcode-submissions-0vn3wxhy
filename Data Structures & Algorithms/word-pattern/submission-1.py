class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst = s.split()
        if len(pattern) != len(lst):
            return False

        dit1 = {}
        dit2 = {}

        for i,ch in enumerate(pattern):
            if ch in dit1:
                if dit1[ch] != lst[i]:
                    return False
                else:
                    continue       
            dit1[ch] = lst[i]

        for i,ele in enumerate(lst):
            if ele in dit2:
                if dit2[ele] != pattern[i]:
                    return False
                else:
                    continue     
            dit2[lst[i]] = pattern[i]

        return True

        
                