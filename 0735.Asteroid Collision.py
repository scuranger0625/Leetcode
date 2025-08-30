from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # 使用堆疊來追踪還在運行的小行星
        stack = []

        # 遍歷每顆小行星
        for asteroid in asteroids:
            # 處理可能發生的碰撞情況
            while stack and asteroid < 0 and stack[-1] > 0:
                if stack[-1] < -asteroid:
                    # 當堆疊頂部的小行星較小，則它會爆炸，繼續比較
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    # 當兩顆小行星大小相等，兩顆都會爆炸
                    stack.pop()
                break
            else:
                # 如果沒有發生碰撞或當前小行星向右移動，則將小行星加入堆疊
                stack.append(asteroid)

        return stack

# 測試範例
solution = Solution()

asteroids1 = [5, 10, -5]
print(solution.asteroidCollision(asteroids1))  # 輸出: [5, 10]

asteroids2 = [8, -8]
print(solution.asteroidCollision(asteroids2))  # 輸出: []

asteroids3 = [10, 2, -5]
print(solution.asteroidCollision(asteroids3))  # 輸出: [10]

asteroids4 = [-2, -1, 1, 2]
print(solution.asteroidCollision(asteroids4))  # 輸出: [-2, -1, 1, 2]
