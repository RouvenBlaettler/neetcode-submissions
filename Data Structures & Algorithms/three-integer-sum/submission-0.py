class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pairs = []
        index1 = -1
        for num in nums:
            index1 += 1
            index2 = -1
            for num in nums:
                index2 += 1
                index3 = -1
                for num in nums:
                    index3 += 1
                    if nums[index1] + nums[index2] + nums[index3] == 0:
                        l = [index1, index2, index3]
                        if len(set(l)) == 3:
                            pair = sorted([nums[index1], nums[index2], nums[index3]])
                            if pair not in  pairs:
                                pairs.append(pair)

        return pairs
