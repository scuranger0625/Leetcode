class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left, right：Binary Search 的搜尋區間邊界
        left = 0
        right = len(nums) - 1

        # 標準 Binary Search 迴圈
        # 只要搜尋區間還存在，就繼續
        while left <= right:
            # 取中間 index
            mid = (left + right) // 2

            # 如果中間值就是 target，直接回傳 index
            if nums[mid] == target:
                return mid

            # -------- 關鍵判斷開始 --------
            # 判斷「哪一半是有序的」

            # 情況 1：左半邊是有序的
            # nums[left] <= nums[mid] 代表 [left, mid] 這段是正常遞增
            elif nums[mid] >= nums[left]:

                # 檢查 target 是否落在左半邊的有序區間內
                # 因為 nums[mid] == target 已經在上面 return 掉
                # 所以這裡寫 <= nums[mid] 在實際執行上是安全的
                if nums[left] <= target <= nums[mid]:
                    # target 在左半邊 → 捨棄右半邊
                    right = mid - 1
                else:
                    # target 不在左半邊 → 去右半邊找
                    left = mid + 1

            # 情況 2：右半邊是有序的
            else:
                # 檢查 target 是否落在右半邊的有序區間內
                if nums[mid] <= target <= nums[right]:
                    # target 在右半邊 → 捨棄左半邊
                    left = mid + 1
                else:
                    # target 不在右半邊 → 去左半邊找
                    right = mid - 1

        # 如果整個 Binary Search 結束仍沒找到 target
        return -1
