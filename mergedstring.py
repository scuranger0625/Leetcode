#當前題目要求將兩個字符串 word1 和 word2 交替合併。
#將兩個字串交替合併，如果其中一個字串較長，則將剩餘的部分添加到最終的合併結果中。

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        #設置列表
        merge = []
        # i,j 在word,word2中 使用zip函數迭代兩筆字串資料 注意zip只能迭代兩筆以上的相同長度資料
        for i,j in zip(word1,word2):
            #merge加入i , j 兩個字串的所有資料
            merge.append(i)
            merge.append(j)

        #如果兩筆字串資料的長度不同時 zip將不會將剩餘的部分合併起來 因此需要:

        # word1如果比word2長 [len(word2):] 從word2長度的地方開始 將剩餘的word1字串加入merge
        merge.append(word1[len(word2):])
        # word2如果比word1長 [len(word1):] 從word1長度的地方開始 將剩餘的word2字串加入merge
        merge.append(word2[len(word1):])

        #返回至   "".join(merge) 將被隔開的字串資料合併成一個新的字串
        return "".join(merge)

            
            


