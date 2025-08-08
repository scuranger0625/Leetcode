class Solution:
    """
    已知最好的解答是不需要跳，或是當首項的值 >= 終點的總長度即代表只需要跳躍一次
    當陣列的相加總合 = 陣列的長度 就代表抵達終點
    也就是說 必須要取 相加次數**最少次**的方式跳躍到終點
    eg.區間擴張貪婪法
    """
    def jump(self, nums: List[int]) -> int:
        # 終點
        n = len(nums)
        # 如果陣列長度為1 不需要跳
        if n == 1:
            return 0
        # 如果首項的值 >= 陣列長度 即代表一步即可跳躍至終點
        if nums[0] >= n-1:
            return 1
        
        jumps = 0 # 跳躍次數
        current_end = 0 # 目前跳躍到的位置
        farthest = 0 # 目前可跳躍的最遠距離

        # 掃到 n-2 即可；最後一格不用掃，避免多算
        for i in range(n - 1):
            # 在當前層內，不斷嘗試把下一層的可達邊界推到最遠
            farthest = max(farthest, i + nums[i])

            # 走到本層邊界 → 這一跳結算，準備換到下一層
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:   # 下一層已覆蓋終點，提前結束
                    break
        return jumps


        
