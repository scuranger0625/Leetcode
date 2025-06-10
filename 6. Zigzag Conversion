class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 如果只有一列 或字串長度長度小於列數 即刻返回
        if numRows == 1 or numRows >= len(s): return s
        # 初始化 row 字串陣列
        rows = ['' for _ in range(numRows)]
        idx, step = 0, 1 # idx 目前字母要放進的row step 下一步要往下還是往上

        for c in s:
            rows[idx] += c # 將當前的idx加入至idx
            # 如果idx裡面沒有東西
            if idx == 0:
                step = 1   # 往下
            # 如果idx已經是最後一列
            elif idx == numRows - 1:
                step = -1  # 往上
            # 決定+1往下 還是-1往上
            idx += step

        return ''.join(rows)
