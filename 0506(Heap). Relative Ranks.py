# Leetcode, ligmaball
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        heap= [] # 建立堆積

        for i in range(n):
            # 因為 heapq 只能每次 pop 出「最小」但我們想要每次拿「最大分數」所以用負號反轉大小：
            heapq.heappush(heap, (-score[i], i))
        
        # 先做一個長度 n 的陣列 之後我們會依名次把字串填進去
        ans = [""]*n
        # 我們準備從第 1 名開始發獎牌/名次
        rank = 1

        while heap:
            _, idx = heapq.heappop(heap)

            if rank ==1:
                ans[idx] = "Gold Medal"
            elif rank ==2:
                ans[idx] = "Silver Medal"
            elif rank ==3:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = str(rank) # 注意：一定要 str(rank) 因為題目要的是字串，不是整數。
                
            rank +=1
            
        return ans
