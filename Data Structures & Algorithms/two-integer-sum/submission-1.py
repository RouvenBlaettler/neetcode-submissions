class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       i1 = -1
       for num1 in nums:
        i1 += 1
        i2 = -1
        for num2 in nums:
            i2 += 1
            if i1 != i2 and num1 + num2 == target:
                return [i1, i2]