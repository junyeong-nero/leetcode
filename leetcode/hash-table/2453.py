class Solution(object):
    def destroyTargets(self, nums, space):
        """
        :type nums: List[int]
        :type space: int
        :rtype: int
        """
        remainder_count = Counter()
        for num in nums:
            remainder_count[num % space] += 1
            
        max_hits = max(remainder_count.values())
        min_seed = float('inf')   
        for num in nums:
            remainder = num % space
            if remainder_count[remainder] == max_hits:
                if num < min_seed:
                    min_seed = num
                    
        return min_seed

