class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0

        for word in words:
            word_count = Counter(word)
            flag = False
            for c in word:
                if word_count[c] <= count[c]:
                    flag = True
                else:
                    flag = False
                    break
            if flag: 
                res += len(word)
        return res