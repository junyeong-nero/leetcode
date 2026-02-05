class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def query(index):
            cur = index
            cur = (index + nums[index] + n) % n
            return nums[cur]
        
        res = [query(i) for i in range(n)]
        return res
                

