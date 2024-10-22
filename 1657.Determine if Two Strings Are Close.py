class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 如果長度不一樣，則不可能是接近的
        if len(word1) != len(word2):
            return False

        # 使用字典來計算字符頻率
        freq1 = {}
        freq2 = {}

        # 計算 word1 中每個字符的頻率
        for char in word1:
            if char in freq1:
                freq1[char] += 1
            else:
                freq1[char] = 1

        # 計算 word2 中每個字符的頻率
        for char in word2:
            if char in freq2:
                freq2[char] += 1
            else:
                freq2[char] = 1

        # 如果兩個字符串的字符集不同，則不能達成接近
        if set(freq1.keys()) != set(freq2.keys()):
            return False

        # 比較字符頻率分佈是否相同
        # 如果兩個字典的值（頻率）排序後相同，則表示可以達成接近
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False

        return True

# 測試範例
solution = Solution()

word1 = "abc"
word2 = "bca"
print(solution.closeStrings(word1, word2))  # 輸出: True

word1 = "a"
word2 = "aa"
print(solution.closeStrings(word1, word2))  # 輸出: False

word1 = "cabbba"
word2 = "abbccc"
print(solution.closeStrings(word1, word2))  # 輸出: True
