# Leetcode, Ligmaball
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten =0,0 # 20元不能找零 不用記
        
        # 第一個不是拿5元 這生意不用做了 直接返回False
        if bills[0]!=5:
            return False

        for i in bills:
            # 先判定拿5元給我的情況 不用找錢
            if i ==5:
                five+=1
            # 繼續判定拿10元找錢的話
            elif i ==10:
                # 判定沒有5元可以找 就直接False
                if five ==0: 
                    return False
                five-=1 # 找5元
                ten+=1  # 多一張10元
            
            # 繼續判定拿20元找的情況
            elif i ==20:
                # 先判定 5元和10元還有的情況 貪婪使用10+5元的方式支付(5元比較萬用)
                if five>0 and ten>0:
                    five-=1 # 找5元
                    ten-=1  # 找10元  
                # 繼續情況 只剩5元可以找
                elif five >=3:
                    five-=3 # 找15元(5*3)
                else:
                    return False
        return True



                

        
        
