# Leetcode, Ligmaball
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 依照「起點 start」排序
        intervals.sort(key=lambda x:x[0]) # 這個排序給了你一個 單調性保證：後面來的區間，start 一定 ≥ 前面的 start
        merged=[]
        # 如果 merged 為空
        # 或是目前區間與最後一個合併區間沒有重疊
        for start, end in intervals:
            if not merged or start > merged[-1][1]: # [-1]:最後一個元素（Python 的負索引） merged[-1] == [15, 18]
                merged.append([start, end]) 
            else:
                merged[-1][1] = max(merged[-1][1], end) # Greedy行為 一旦你決定某些區間要合併，就「立刻、永久」把它們合成一個最大的區間

        return merged





        

        
