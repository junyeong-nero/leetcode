class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        # nums[i] < nums[j] > nums[k]

        prefix_left = [float("inf")]
        prefix_right = [float("inf")]
        for num in nums:
            prefix_left.append(min(prefix_left[-1], num))
        
        for num in nums[::-1]:
            prefix_right.append(min(prefix_right[-1], num))
        
        prefix_right = prefix_right[::-1]

        # prefix-left = min(nums[:i])
        # prefix-right = min(nums[i:])
        # print(prefix_left)
        # print(prefix_right)

        n = len(nums)
        res = float("inf")

        for j in range(1, n - 1):
            left = prefix_left[j]
            right = prefix_right[j + 1]
            if left < nums[j] > right:
                temp = left + nums[j] + right
                res = min(res, temp)

        return -1 if res == float("inf") else res
