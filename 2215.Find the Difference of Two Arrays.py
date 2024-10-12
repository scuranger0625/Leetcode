from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # 使用 set 去重並求差集
        set1 = set(nums1)  # nums1 中的獨特元素
        set2 = set(nums2)  # nums2 中的獨特元素

        # 找出 nums1 中有但不在 nums2 中的元素
        result1 = list(set1 - set2)

        # 找出 nums2 中有但不在 nums1 中的元素
        result2 = list(set2 - set1)

        # 返回兩個結果列表
        return [result1, result2]
