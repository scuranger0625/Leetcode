class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 1) 先看整體能不能走一圈
        if sum(gas) < sum(cost):
            return -1
        
        # 2) 初始化兩個狀態變數
        start = 0   # 起始站位置
        tank = 0    # 油箱目前累積油量
        
        # 3) 用 index 線性掃一圈，模擬「每到一站加油，再扣掉開到下一站的花費」
        n = len(gas)
        for i in range(n):
            tank += gas[i] - cost[i]
            # 4) 如果 tank < 0 代表從當前 start 走到 i 會爆油
            #    → 把起點換成 i+1，油箱重置成 0，重新累計
            if tank < 0:
                start = i + 1
                tank = 0
        
        # 5) 掃完一圈都沒爆炸，那唯一的 start 就是解
        return start
