class Solution:
    def removeStars(self, s: str) -> str:
        # 使用列表作為堆疊
        stack = []

        # 遍歷字符串
        for char in s:
            if char == '*':
                # 如果是星號，彈出棧頂元素
                if stack:
                    stack.pop()
            else:
                # 如果不是星號，壓入棧中
                stack.append(char)

        # 最後棧中的元素組成最終結果
        return ''.join(stack)

# 測試範例
solution = Solution()

s1 = "leet**cod*e"
print(solution.removeStars(s1))  # 輸出: "lecoe"

s2 = "erase*****"
print(solution.removeStars(s2))  # 輸出: ""
