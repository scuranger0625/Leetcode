public class Solution {
    // 主方法：判斷是否能在 k 次操作內將陣列全部元素變成相同（1 或 -1）
    public boolean canMakeEqual(int[] nums, int k) {
        // 嘗試將陣列全部變成 target（1 或 -1）
        return tryMakeAll(nums, k, 1) || tryMakeAll(nums, k, -1);
    }

    // 輔助函式：嘗試把 nums 變成全 target
    private boolean tryMakeAll(int[] nums, int k, int target) {
        int n = nums.length;
        int[] arr = new int[n];
        System.arraycopy(nums, 0, arr, 0, n); // 複製陣列，避免改動原陣列

        int operations = 0; // 操作計數

        // 從左往右遍歷，碰到不符合 target 的位置就翻轉該位置與下一位置的符號
        for (int i = 0; i < n - 1; i++) {
            if (arr[i] != target) {
                arr[i] = -arr[i];
                arr[i + 1] = -arr[i + 1];
                operations++;
                if (operations > k) {
                    return false; // 操作超過限制，失敗
                }
            }
        }

        // 最後檢查最後一個元素是否為 target，且操作數不超過 k
        return arr[n - 1] == target && operations <= k;
    }
}
