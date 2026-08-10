class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        for num1 in numbers:
            index2 = 0
            index1 += 1
            for num2 in numbers:
                index2 += 1
                if num1 + num2 == target and index1 != index2:
                    return [index1, index2]

                