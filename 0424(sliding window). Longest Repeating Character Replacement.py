class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l=0
        window = {}
        res = 0
        max_freq = 0

        for r in range(n):
            char_r = s[r]
            window[char_r]=window.get(char_r,0)+1
            max_freq = max(max_freq, window[char_r])

            # 不符合要求 While迴圈收縮左邊界
            
            while (r - l + 1) - max_freq > k: # 窗口長度減去出現最多次的頻率，如果剩下的字元超過 k，代表不能被替換掉
                char_l = s[l]
                window[char_l]-=1
                # 如果window數量歸0 字典要刪除key
                if window[char_l]==0:
                    del window[char_l]
                l +=1
            
            res = max(res,r-l+1)
        
        return res


