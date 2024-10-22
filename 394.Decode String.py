class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                # 如果是數字，計算重複次數
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # 將當前字符串和次數壓入堆疊
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0
            elif char == ']':
                # 從堆疊中彈出之前的字符串和次數
                prev_string, num = stack.pop()
                current_string = prev_string + current_string * num
            else:
                # 普通字符添加到當前字符串
                current_string += char

        return current_string