class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total_len = m + n
        half_len = total_len // 2

        # 指標 i 和 j 用來遍歷 nums1 和 nums2
        i = j = 0
        merged = []  # 存放合併後的元素
        
        # 合併兩個數組直到合併到一半
        while len(merged) <= half_len:
            if i < m and (j >= n or nums1[i] <= nums2[j]):
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # 如果總長度是奇數，中位數就是中間的元素
        if total_len % 2 == 1:
            return merged[half_len]
        # 如果總長度是偶數，中位數是中間兩個元素的平均
        else:
            return (merged[half_len - 1] + merged[half_len]) / 2
