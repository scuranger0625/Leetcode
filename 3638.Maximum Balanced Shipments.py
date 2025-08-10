class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        
        count = 0 # 計數器
        
        batch_max = None # 當前批次的最大值；None 表示尚未開批次

        for w in weight:
            if batch_max is None:
                batch_max = w
            
            elif w < batch_max:
                count += 1
                batch_max = None # 重置下一次的批次最大重量值
            else:
                batch_max = w if w > batch_max else batch_max

        return count







     
