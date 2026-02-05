class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()

        @cache
        def dfs(cur):
            if cur in visited:
                return False
            if not (0 <= cur < n):
                return False
            if arr[cur] == 0:
                return True

            visited.add(cur)
            return dfs(cur + arr[cur]) or dfs(cur - arr[cur])

        return dfs(start)
