class Solution:
    def reverseWords(self, s: str) -> str:
        
        # 使用split()分割字串成單詞列表，split()會自動去除多餘的空格
        words = s.split()
        
        # 使用[::-1]將單詞列表反轉
        reversed_words = words[::-1]
        
        # 使用join()將單詞列表用單一空格連接成新的字串
        reversed_string = ' '.join(reversed_words)
        return reversed_string
