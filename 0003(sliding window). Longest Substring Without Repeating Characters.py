class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left= 0
        res= 0
        count={} # 計數器
        unique_count = 0 # type int

        for right in range(n):
            char_r = s[right]
            count[char_r] = count.get(char_r,0)+1

            unique_count +=1 # 不重複字串+1

            while count[char_r] > 1: # 違法邊界條件 while迴圈
                char_l = s[left]
                count[char_l] -= 1 
                # 歸零時必須從字典裡徹底刪除
                if count == 0:
                    del count[char_r]
                left += 1
            res = max(res,right-left+1)
        
        return res

