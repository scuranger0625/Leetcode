class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)

        # 用 list 模擬 linked list，每個數字當作一個「節點」
        digits = []
        while x > 0:
            digits.append(x % 10)  # 把個位數當成節點塞進 list
            x //= 10

        # 用多項式展開（digits 本身已經是反轉順序）
        rev = 0
        for d in digits:
            # 判斷是否會 overflow
            if rev > (INT_MAX - d) // 10:
                return 0
            rev = rev * 10 + d

        return sign * rev
