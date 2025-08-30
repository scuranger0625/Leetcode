class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # 初始化窗口的左邊界
        left = 0
        # 計算當前窗口內的 0 的數量
        zero_count = 0
        # 用來存儲最大連續 1 的長度
        max_length = 0

        # 遍歷整個數組，right 是窗口的右邊界
        for right in range(len(nums)):
            # 如果遇到 0，將 zero_count 增加
            if nums[right] == 0:
                zero_count += 1

            # 當窗口內的 0 的數量超過 k 時，移動左邊界
            while zero_count > k:
                # 如果左邊界是 0，減少 zero_count
                if nums[left] == 0:
                    zero_count -= 1
                # 移動左邊界
                left += 1

            # 計算當前合法窗口的長度，更新 max_length
            max_length = max(max_length, right - left + 1)

        # 返回可以獲得的最大連續 1 的長度
        return max_length
