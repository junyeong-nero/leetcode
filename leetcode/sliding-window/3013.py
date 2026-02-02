from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        # We need to pick nums[0] and then k-1 more elements.
        # One of those k-1 elements must be nums[i] (the start of the 2nd subarray).
        # The remaining k-2 elements must be chosen from the window of size 'dist'.
        
        target_count = k - 2
        # current_window_sum tracks the sum of the 'target_count' smallest elements
        current_window_sum = 0
        
        # small: the target_count smallest elements
        # large: the rest of the elements in the sliding window
        small = SortedList()
        large = SortedList()
        
        def add(val):
            nonlocal current_window_sum
            small.add(val)
            current_window_sum += val
            if len(small) > target_count:
                removed = small.pop(-1)
                current_window_sum -= removed
                large.add(removed)
                
        def remove(val):
            nonlocal current_window_sum
            if val in small:
                small.remove(val)
                current_window_sum -= val
                if large:
                    added = large.pop(0)
                    small.add(added)
                    current_window_sum += added
            else:
                large.remove(val)

        # Initial window setup: indices [1, 1 + dist]
        # But wait, nums[i] is the start of the 2nd subarray. 
        # The window for the other k-2 elements is nums[i+1 : i+dist+1]
        
        # Let's simplify: We pick nums[0], then we need to pick k-1 elements 
        # from nums[1:] such that the index difference is <= dist.
        # This is equivalent to a sliding window of size dist + 1 
        # where we pick the smallest k-1 elements.
        
        ans = float('inf')
        window_size = dist + 1
        target_count = k - 1
        
        for i in range(1, n):
            add(nums[i])
            
            # When the window is full (we've processed at least 'dist + 1' elements)
            # or we've reached the point where a window can exist
            if i >= window_size:
                # The window starts at i - dist. We need to remove the element that is
                # now outside the window starting from the next iteration.
                if len(small) == target_count:
                    ans = min(ans, nums[0] + current_window_sum)
                
                remove(nums[i - dist])
            elif i == n - 1 or i >= target_count: # Handle cases where window isn't full yet
                 if len(small) == target_count:
                    ans = min(ans, nums[0] + current_window_sum)
                    
        return ans
