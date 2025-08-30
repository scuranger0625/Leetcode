class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)  # 將字符串轉換為列表，因為字符串是不可變的
        
        # left為從列表的開頭開始 right代表從列表的最後一個開始
        left, right = 0, len(s) - 1

        while left < right:
            # not in 是 Python 中的一個運算符，用於檢查一個元素是否不在某個集合（如列表、元組、集合、字典的鍵等）中。
            # 如果元素不在集合中，not in 表達式的結果為 True；如果元素在集合中，結果為 False。
            
            #如果left部分的字母不在vowels中  left +1
            if s[left] not in vowels:
                left += 1
            #如果right部分的字母不在vowels中  right -1
            elif s[right] not in vowels:
                right -= 1
            else:
                # 交換元音字母
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)
