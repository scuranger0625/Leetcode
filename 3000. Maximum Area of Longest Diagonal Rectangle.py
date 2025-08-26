from typing import List

class Solution:

    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:    
        # 目前最長對角線及最大面積
        max_diag_sq = 0
        best_area = 0
        
        for l, w in dimensions:
            diag_sq = l*l + w*w
            area = l*w

            # 狀態更新
            if diag_sq > max_diag_sq:
                max_diag_sq = diag_sq
                best_area = area

            if diag_sq == max_diag_sq and area > best_area:
                best_area = area
                
        return best_area
        



                


            

        
