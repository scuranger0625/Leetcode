# Leetcode, Ligmaball
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1]) 
        arrow = 1 # 至少會射出一支箭
        curr_end = points[0][1] # 當前氣球的最右邊
        n =len(points)
        for i in range(n):
            # 若氣球左邊(對所有氣球)比當前氣球的右邊更大時(代表沒交集)
            if points[i][0] > curr_end: 
                arrow+=1
                curr_end = points[i][1] # 更新當前氣球指標
        
        return arrow





        
