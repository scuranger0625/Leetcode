class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        n = len(value)
        groups = [] # 建立空的分桶

        # 建立n+1個空桶
        for _ in range(n+1): # 如果你不打算用這個變數 慣例是用 _ 代替
            groups.append([])
        # 迭代value limit雙陣列
        for v, l in zip(value,limit):
            # 貪婪法 將value 丟入當前的桶中
            groups[l].append(v)

        # 計算最大value
        total = 0
        for l in range(1, n+1): # 優先貪limit 放在外層迴圈
            if groups[l]:
                groups[l].sort(reverse=True) # reverse=True → 讓排序結果反過來，變成 由大到小排列
                # 取分桶中最小的limit數量
                take_count = min(l, len(groups[l]))
                # 最大值取 limit最小桶中的value 直到take_count最大值
                total += sum(groups[l][:take_count])
        
        return total
                

