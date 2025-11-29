class Solution:
    # 不可以直接用迭代刪除val
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for idx, x in enumerate(nums): # enumerate(nums) 會同時取得index , value
            if x != val:
                nums[k] = x
                k += 1
        return k
                
            




                
        
