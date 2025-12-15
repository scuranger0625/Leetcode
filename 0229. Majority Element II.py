class Solution:
    def majorityElement(self, nums):
        # 第一階段：找「最多兩個可能的候選人」
        cand1 = cand2 = None
        cnt1 = cnt2 = 0

        for x in nums:
            if x == cand1:
                cnt1 += 1
            elif x == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1 = x
                cnt1 = 1
            elif cnt2 == 0:
                cand2 = x
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        # 第二階段：重新計數，確認誰真的超過 n/3
        res = []
        n = len(nums)

        if nums.count(cand1) > n // 3:
            res.append(cand1)
        if cand2 is not None and nums.count(cand2) > n // 3:
            res.append(cand2)

        return res
