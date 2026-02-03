import heapq

class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)
        # 1. (nums1값, nums2값, 원래 인덱스) 튜플 생성 후 nums1 기준으로 정렬
        combined = []
        for i in range(n):
            combined.append((nums1[i], nums2[i], i))
        combined.sort()
        
        res = [0] * n
        min_heap = []
        current_sum = 0
        
        # 2. 정렬된 리스트를 순회하며 결과 계산
        # j는 '현재 숫자보다 작은 숫자들'을 가리키는 포인터
        j = 0
        for i in range(n):
            curr_v1, curr_v2, curr_idx = combined[i]
            
            # nums1[j] < nums1[i] 인 모든 j에 대해 nums2[j]를 힙에 추가
            while j < i and combined[j][0] < curr_v1:
                val_to_add = combined[j][1]
                heapq.heappush(min_heap, val_to_add)
                current_sum += val_to_add
                
                # 힙 크기가 k를 넘으면 가장 작은 값 제거
                if len(min_heap) > k:
                    current_sum -= heapq.heappop(min_heap)
                j += 1
            
            # 현재까지 쌓인 힙의 합(가장 큰 k개의 합)이 곧 정답
            res[curr_idx] = current_sum
            
        return res
