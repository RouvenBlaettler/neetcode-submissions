class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def product(nums):
            total = 1
            for num in nums:
                total *= num
            return total
        l = []
        counter = -1
        for num in nums:
            counter += 1
            new_nums = nums[:counter] + nums[counter+1:]
            l.append(product(new_nums))
        return l