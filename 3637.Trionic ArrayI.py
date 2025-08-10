class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        # 若陣列長度 <3 那就甭談三段陣列了
        if n < 3 :
            return False
        
        # 設置狀態機 
        i = 0
        s1 = s2 = s3 = 0 # 三段陣列各自的單調步數

        # 同時必須滿足index 和value是嚴格遞增的
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
            s1 += 1

        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
            s2 += 1
        
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
            s3 += 1
        
        # 必須剛好吃完整個陣列，且每段至少 1 步（嚴格單調、避免空段）
        return i == n - 1 and s1 > 0 and s2 > 0 and s3 > 0
        
        
