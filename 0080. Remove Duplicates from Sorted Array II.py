class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0 # 寫入的位置
        for x in nums:
            if k < 2 or x != nums[k-2]:
                nums[k] = x # 該寫入位置的 value變為x
                k += 1 # 換下一個寫入的位置
        
        return k

# Leetcode not only poor but aslo fucking stipid

                
        
