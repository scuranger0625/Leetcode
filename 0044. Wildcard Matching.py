class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0                  # i 指向 s，j 指向 p
        star_idx = -1              # 記錄最近出現的 * 在 p 中的位置
        match = 0                  # 記錄當前 * 對應到 s 的哪個位置

        while i < len(s):
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                # 當字元相同 或 pattern 是 '?' 時，兩個都往右移
                i += 1
                j += 1

            elif j < len(p) and p[j] == '*':
                # 遇到 '*'，先記下 * 的位置與 s 當前的位置
                star_idx = j
                match = i
                j += 1             # 嘗試讓 '*' 先配 0 個字元

            elif star_idx != -1:
                # 如果之前遇過 *，現在 pattern 不匹配
                # 回退：讓 * 多匹配一個 s 中的字元
                j = star_idx + 1
                match += 1
                i = match

            else:
                # 既不是字元匹配、也沒 * 可以回退 → 失敗
                return False

        # 檢查 pattern 是否還有多餘的 *
        while j < len(p) and p[j] == '*':
            j += 1

        # 若 pattern 也走完，則匹配成功
        return j == len(p)
