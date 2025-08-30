class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 1. 計算每個元素的出現次數
        count = Counter(arr)
        
        # 2. 檢查是否有重複的出現次數
        seen = set()
        for freq in count.values():
            if freq in seen:
                return False  # 一旦發現重複次數，立即返回 False
            seen.add(freq)  # 如果沒有重複，則加入 seen 集合
        
        # 3. 如果遍歷完畢沒有重複，返回 True
        return True
