# Leetcode, Ligmaball
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1,-1,-1): # 從最後一位開始往前掃（模擬手算加法）
            # 如果這一位不是 9 → 不會產生進位
            if digits[i]<9:
                digits[i]+=1  # 直接 +1
                return digits # 任務完成，直接回傳
            
            digits[i]=0       # 如果是 9 → 9 + 1 = 10 這一位要變成 0，並把進位往前傳

        # 如果整個迴圈跑完，代表原本每一位都是 9 例如 [9,9,9] → [0,0,0] 需要在最前面補一個 1 → [1,0,0,0]
        return [1]+digits

        
