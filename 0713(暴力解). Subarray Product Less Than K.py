# 暴力解（O(n²)，一定 TLE
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        n = len(nums)
        count = 0

        # 固定左端點 i
        for i in range(n):
            product = 1

            # 右端點 j 往右展開
            for j in range(i, n):
                product *= nums[j]

                if product < k:
                    count += 1
                else:
                    # 注意：這裡可以 break，但就算不 break 也還是暴力
                    break

        return count
