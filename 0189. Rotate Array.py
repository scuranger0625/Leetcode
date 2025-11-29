class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # 避免 k > n
        """
        Do not return anything, modify nums in-place instead.
        """
        # 反轉函式（in-place）
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        # 1️ 反轉整個陣列
        reverse(0, n - 1)

        # 2️ 反轉前 k 個
        reverse(0, k - 1)

        # 3️ 反轉剩下的
        reverse(k, n - 1)
