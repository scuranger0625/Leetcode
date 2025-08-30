#當兩個字符串 s 和 t 時，我們說 "t 能整除 s"，當且僅當 s 是由一個或多個 t 拼接而成的（即 s = t + t + t + ... + t + t）。
#給定兩個字符串 str1 和 str2，返回一個最大的字符串 x，使得 x 能整除 str1 和 str2。

#將兩筆字串資料重複的部分變成一個新的字串 其餘的排除掉

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # !=為比較運算符，用於檢查兩個值是否不相等。當運算符兩邊的值不相等時，表達式返回 True，否則返回 False
        if str1 + str2 != str2 + str1:
            #返回一個空白字串
            return ""
        
        # math.gcd用於計算兩個數字的最大公因數
        gcd_len = math.gcd(len(str1), len(str2))
        
        # 返回 str1 的前 gcd_len 個字符作為結果
        return str1[:gcd_len]
