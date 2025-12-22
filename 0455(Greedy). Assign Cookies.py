class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort() # 需求
        s.sort() # 資源

        i, j =0, 0
        while i <len(g) and j <len(s): 
            # 如果當前資源能滿足目前最小的需求
            if s[j]>=g[i]: 
                i+=1 # 滿足了一個需求
            j+=1 # 無論有沒有滿足，資源都消耗掉了(或看下一個資源)
        return i
        
