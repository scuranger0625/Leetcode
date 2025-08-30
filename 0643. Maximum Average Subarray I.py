class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 初始計算前 k 個元素的總和，這是我們的第一個窗口
        current_sum = sum(nums[:k])  
        # 將這個總和當作當前最大的總和
        max_sum = current_sum

        # 從索引 k 開始，逐個滑動窗口直到陣列的結尾
        for i in range(k, len(nums)):
            # 更新窗口總和：移除窗口最左邊的元素，加入窗口最右邊的新元素
            current_sum += nums[i] - nums[i - k]
            # 檢查當前窗口的總和是否比之前的最大總和大，如果是，更新最大總和
            max_sum = max(max_sum, current_sum)

        # 最後，將最大總和除以 k，得到最大平均值並回傳
        return max_sum / k
