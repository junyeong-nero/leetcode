from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        # Find the end of the first strictly increasing segment (index p)
        p = 0
        while p + 1 < n and nums[p] < nums[p + 1]:
            p += 1
        
        # p must be at least 1 and leave room for q and the last segment
        if p == 0 or p > n - 3:
            return False
        
        # Find the end of the strictly decreasing segment starting at p (index q)
        q = p
        while q + 1 < n and nums[q] > nums[q + 1]:
            q += 1
        
        # q must be greater than p and strictly before the last index
        if q == p or q >= n - 1:
            return False
        
        # Verify that the remaining part is strictly increasing
        for i in range(q, n - 1):
            if nums[i] >= nums[i + 1]:
                return False
        
        return True

# class Solution:
#     def isTrionic(self, nums: List[int]) -> bool:
#         section = 0

#         def check(arr):
#             m = len(arr)
#             for i in range(m - 1):
#                 if arr[i] >= arr[i + 1]:
#                     return False
#             return True

#         n = len(nums)
#         for p in range(1, n - 2):
#             for q in range(p + 1, n - 1):
#                 a = check(nums[:p + 1])
#                 b = check(nums[p:q + 1][::-1])
#                 c = check(nums[q:])
#                 if a and b and c:
#                     return True

#         return False
                
