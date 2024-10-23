from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # 初始化兩個隊列，分別記錄 'R' 和 'D' 的索引位置
        radiant = deque()
        dire = deque()

        # 遍歷輸入字串，將 'R' 和 'D' 的索引加入對應的隊列
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        n = len(senate)

        # 進行投票過程的模擬
        while radiant and dire:
            r = radiant.popleft()  # 取得最前面的 'R' 議員索引
            d = dire.popleft()     # 取得最前面的 'D' 議員索引

            # 比較 'R' 和 'D' 的索引位置，選擇優先禁權的議員
            if r < d:
                # 'R' 在前面，因此禁止 'D'，並將自己加入下一輪
                radiant.append(r + n)
            else:
                # 'D' 在前面，因此禁止 'R'，並將自己加入下一輪
                dire.append(d + n)

        # 判斷獲勝者
        return "Radiant" if radiant else "Dire"
