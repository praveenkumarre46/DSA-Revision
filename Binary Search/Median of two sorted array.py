class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        total_len = n1 + n2
        target_idx = total_len // 2
        
        i = j = 0
        m1 = m2 = 0
        
        for count in range(target_idx + 1):
            m2 = m1
            if i < n1 and (j >= n2 or nums1[i] <= nums2[j]):
                m1 = nums1[i]
                i += 1
            else:
                m1 = nums2[j]
                j += 1
        
        if total_len % 2 == 1:
            return float(m1)
        return (m1 + m2) / 2.0