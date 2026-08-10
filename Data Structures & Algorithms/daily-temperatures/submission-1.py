class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmer_days = []
        index = 0
    
        for t1 in temperatures:
            index += 1
            amount = 0
            breaks = 0
            for t2 in temperatures[index:]:
                amount += 1
                if t2 > t1:
                    breaks = 1
                    break
            if not breaks:
                amount = 0

            warmer_days.append(amount)


        
        
        return warmer_days
                
        