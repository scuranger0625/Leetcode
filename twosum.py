#題目描述：
#你有一個數字列表 nums，裡面包含了一些整數。
# 你還有一個目標數字 target。你的任務是從這個數字列表中找到兩個數字，它們相加的和剛好等於 target。然後，你要返回這兩個數字在列表中的位置（索引）。
#具體要求：
#每個數字只能使用一次。
#保證一定會有一個解，所以你不用擔心找不到答案。
#返回的答案可以是任意順序的。

# 導入 List 類型提示
from typing import List  

#定義一個名為Solution的方法
class Solution:
    #採用一個名為twosum的計算方法和值 包括自身,數字列表 以及目標數字target   -> List[int]返回列表
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #設置字典
        index={} 
        #當 i 以及 列表nums時 於enumerate(nums) 獲取list中的值和位置
        for i, nums in enumerate(nums):
            #虛設complement為target-nums所得到的數字 
            complement = target - nums   
            # 如果complement在字典index中
            if complement in index:       
                #返回列表化的 index的數字complement和找到的數字i
                return[index[complement],i]  
           # 將當前數字及其索引存入字典
            index[nums] = i  

            

            
