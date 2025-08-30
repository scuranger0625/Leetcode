class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # 定義元音字母集合
        vowels = set('aeiou')
        
        # 初始化窗口內的元音數量，計算前 k 個字符中的元音數量
        current_vowel_count = sum(1 for i in range(k) if s[i] in vowels)
        # 初始化最大元音數量
        max_vowels = current_vowel_count
        
        # 使用滑動窗口，從索引 k 開始直到字串結尾
        for i in range(k, len(s)):
            # 如果窗口的左端字符是元音，移出時減少元音計數
            if s[i - k] in vowels:
                current_vowel_count -= 1
            # 如果窗口的右端新加入的字符是元音，加入時增加元音計數
            if s[i] in vowels:
                current_vowel_count += 1
            # 更新最大元音數量
            max_vowels = max(max_vowels, current_vowel_count)
        
        # 返回最大元音數量
        return max_vowels
