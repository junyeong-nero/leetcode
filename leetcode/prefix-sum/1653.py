class Solution:
    def minimumDeletions(self, s: str) -> int:
        left, right = 0, s.count("a")
        res = left + right
        for c in s:
            if c == "a":
                right -= 1
            if c == "b":
                left += 1
            res = min(res, left + right)

        return res
