class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)

        res = 0
        index = 0
        for char, freq in counter.most_common():
            cost = 1
            if 8 <= index < 16:
                cost = 2
            if 16 <= index < 24:
                cost = 3
            if 24 <= index:
                cost = 4
            
            res += freq * cost
            index += 1

        return res
                                
