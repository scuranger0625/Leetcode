class Solution:
    def maxDifference(self, s: str) -> int:
        # 初始化 26 個英文字母的頻率表
        freq = [0] * 26

        # 掃過一次字串，統計頻率
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        max_odd = -1
        min_even = float('inf')

        for f in freq:
            if f == 0:
                continue
            if f % 2 == 1:  # 奇數
                max_odd = max(max_odd, f)
            else:  # 偶數
                min_even = min(min_even, f)

        return max_odd - min_even
