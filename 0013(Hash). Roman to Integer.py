# Leetcode, Ligmaball
class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        # 查表
        val= {"I":1, "V":5, "X":10, "L":50,
        "C":100, "D":500, "M":1000
    }

        total = 0

        for i in range(n):
            # 如果下一個字比較大 就減
            if i+1 < n and val[s[i]] < val[s[i+1]]:
                total -= val[s[i]]
            else:
                # 否則就加
                total += val[s[i]]

        return total

        
