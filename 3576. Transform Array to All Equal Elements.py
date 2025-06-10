class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        # 定義輔助函式，嘗試將陣列全部變成指定目標值 target (1 或 -1)
        def try_make_all(target: int) -> bool:
            arr = nums[:]  # 複製陣列，避免修改原始輸入
            operations = 0  # 紀錄已執行的操作次數
            n = len(arr)    # 取得陣列長度

            # 從左到右逐個檢查元素，最後一個元素無法再翻轉後面相鄰元素，故遍歷到倒數第二個元素
            for i in range(n - 1):
                # 若當前元素不等於目標值，代表需要進行翻轉操作
                if arr[i] != target:
                    # 同時將當前元素與下一個元素的符號反轉（乘以 -1）
                    arr[i] = -arr[i]
                    arr[i + 1] = -arr[i + 1]
                    operations += 1  # 操作次數加 1
                    
                    # 若操作次數超過限制 k，提前結束並回傳 False
                    if operations > k:
                        return False
            
            # 最後檢查最後一個元素是否也符合目標值，且操作次數不超過 k
            return arr[-1] == target and operations <= k
        
        # 嘗試兩種目標：將陣列全部變成 1 或全部變成 -1，
        # 任一條件成立即回傳 True，否則回傳 False
        return try_make_all(1) or try_make_all(-1)
