class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # 如果陣列長度== 1 直接回傳True
        if n == 1:
            return True
        # 在陣列長度不是1的情況下 首項為0直接回傳False
        if nums[0] == 0:
            return False
        
        # 目前能跳躍到的最遠距離
        maxReach = 0 
        i = 0
        # 同時取得nums陣列的index位置以及值value (enumerate會先取index 再取value)
        for i , step in enumerate(nums):
            # 若要跳躍的位置於最大跳躍距離之外 (跳不到)
            if i > maxReach:
                return False
            
            # 更新當前位置可以跳躍的最大距離
            maxReach = max(maxReach, i + step)
            
            # 若最大跳躍距離比陣列的長度還長 (可直接跳到終點)
            if maxReach >= n - 1:
                return True
            # 能掃完代表可以達到終點
        return True
