public class Solution {
    // 主方法，判斷是否能在最多 k 次操作後，將陣列 nums 全部元素變成相同值（1 或 -1）
    public bool CanMakeEqual(int[] nums, int k) {
        // 內部輔助函式，嘗試將陣列全部變成目標值 target（1 或 -1）
        bool TryMakeAll(int target) {
            int n = nums.Length;               // 取得陣列長度
            int[] arr = new int[n];            
            nums.CopyTo(arr, 0);               // 複製一份陣列，避免修改原陣列

            int operations = 0;                // 紀錄目前已執行的操作次數

            // 從左到右掃描陣列（到倒數第二個元素），進行符號調整
            for (int i = 0; i < n - 1; i++) {
                // 如果目前元素不等於目標值，就需對 i 和 i+1 位置做符號翻轉操作
                if (arr[i] != target) {
                    // 將 arr[i] 與 arr[i + 1] 同時乘以 -1（符號反轉）
                    arr[i] = -arr[i];
                    arr[i + 1] = -arr[i + 1];

                    operations++;              // 操作次數加 1

                    // 若操作次數超過 k，代表無法在限制內完成目標，直接返回 false
                    if (operations > k) {
                        return false;
                    }
                }
            }

            // 最後檢查陣列最後一個元素是否為目標值，因為最後一個元素無法再被翻轉修正
            // 且確保操作次數沒超過 k
            return arr[n - 1] == target && operations <= k;
        }

        // 嘗試兩種目標：全部變成 1 或全部變成 -1，只要其中一種成功即返回 true
        return TryMakeAll(1) || TryMakeAll(-1);
    }
}
