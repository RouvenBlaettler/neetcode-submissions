class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        amounts = {}
        res = []
        for num in set(nums):
            amount = nums.count(num)
            amounts[num] = amount
        ranked = reversed(sorted(amounts.items(), key = lambda x:x[1]))
        for key, val in ranked:
            res.append(key)
            if len(res) == k:
                return res



        