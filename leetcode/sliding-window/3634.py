from typing import List
import bisect

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        max_keep = 0
        left = 0
        
        # 각 left 포인터에 대해 조건을 만족하는 가장 먼 right를 찾습니다.
        for right in range(n):
            # 조건: max_val <= min_val * k
            # 만약 조건을 어기면 left를 전진시켜 범위를 좁힙니다.
            while nums[right] > nums[left] * k:
                left += 1
            
            # 현재 [left, right] 구간은 조건을 만족함
            # 이 구간의 길이를 측정해 최대 유지 개수를 갱신
            max_keep = max(max_keep, right - left + 1)
            
        return n - max_keep

# class Solution:
#     def minRemoval(self, nums: List[int], k: int) -> int:
#         # max-value <= min-value * k
#         # remove all max numbers max-value > min-value * k
#         # or 
#         # remove all min numbers  min-value < max-value / k
#         min_value = min(nums)
#         max_value = max(nums)
#         n = len(nums)

#         nums = sorted(nums)
#         min_delete = bisect_right(nums, max_value / k)
#         max_delete = n - bisect_right(nums, min_value * k)

#         # print(min_delete, max_delete)

#         return min(min_delete, max_delete)
