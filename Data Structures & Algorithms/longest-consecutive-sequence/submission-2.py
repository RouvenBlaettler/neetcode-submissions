class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        l = sorted(list(set(nums)))
        if not l:
            return 0
        print(l)
        prev_num = -10000
        counter = 1
        counters = []
        for num in l:
            if prev_num + 1 == num:
                counter += 1
                counters.append(counter)
            else:
                counters.append(counter)
                counter = 1
            prev_num = num

        return max(counters)
            
