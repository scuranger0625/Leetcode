class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # 用來存儲當前窗口內的字符
        left = 0  # 左指針，表示窗口的左邊界
        max_length = 0  # 用來記錄最長子字串的長度

        # 遍歷字串，right 是滑動窗口的右指針
        for right in range(len(s)):
            # 當遇到重複字符，移動左指針，直到移除重複字符
            while s[right] in char_set:
                char_set.remove(s[left])  # 從集合中移除最左邊的字符
                left += 1  # 移動左指針

            # 將當前字符加入集合
            char_set.add(s[right])

            # 更新最大子字串長度
            max_length = max(max_length, right - left + 1)

        return max_length
